# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Forgotten Among the Fallen** is a dark fantasy Viking text-adventure game (Flask/Python backend + vanilla JS frontend). Players wake as a Viking ghost in a liminal space between life and death, navigating moral choices, combat, and narrative consequences.

## Commands

**Run locally:**
```bash
pip install flask>=3.0.0
python app.py
# Available at http://localhost:5000
```

**Run with Docker:**
```bash
docker compose up --build
```

**Environment variables:** `PORT` (default 5000), `FLASK_ENV`, `SECRET_KEY`

There are no tests or build tools configured. Run after every code change:

```bash
python -m black engine/ content/ app.py
prettier --write static/js/
python -m ruff check engine/ content/ app.py
```

F8xx ruff errors are real bugs and must be fixed. E4xx/E7xx are style only.

## Architecture

**Backend (Python/Flask) — `app.py`**
- Stateless HTTP server; player state lives in Flask session (not database)
- State serialized/deserialized as `PlayerState` dataclass on every request
- API routes: `/api/new`, `/api/load`, `/api/scene`, `/api/choose`, `/api/combat/action`, `/api/advance`, `/api/status`

**Game Engine — `engine/`**
- `state.py`: `PlayerState` dataclass. Stats, inventory, flags, memory fragments, save/load. Derived threshold methods (`is_cursed` etc.) read thresholds from `STATS` config.
- `scene.py`: Processes scene beats and returns JSON. Side effects apply only on first visit. Auto-advances scenes with no prose/choices/combat.
- `combat.py`: Turn-based combat engine. Player actions: light/heavy strike, parry, flank, runic burst, mercy, flee. All numeric thresholds live in `COMBAT_CONFIG`; narrative strings in `combat_prose.py`. Status effects applied via `_apply_effect()` registry helper.
- `dice.py`: `roll(sides)`, `roll_range(lo, hi)`, `chance(p)` — shared across engine.
- `conditions.py`: Data-driven condition evaluator used by scene and choice visibility logic.

**Game Config — `content/game_config.py`**
- `STATS`: per-stat bounds (`min`/`max`/`default`) and derived thresholds (`threshold`)
- `EQUIPMENT`: all equippable items with `slot`, `tier`, and slot-specific properties (`damage_bonus` for weapons, `defense` for shields, `berserk` for body). Auto-equip is tier-based.
- `COMBAT_CONFIG`: all numeric combat constants. `actions` sub-dict groups per-action values (`dmg`, `wrath`, `cost`, etc.). Top-level keys: `curse_damage_scale`, `phase2/3_hp_ratio`, `bleeding`, `taunt_chance`, etc.
- `COMBAT_MODS`: stat-based damage modifiers applied after equipment bonuses.
- `EFFECTS`: status effect registry — `{"bleeding": {"dmg": (4,8), "duration": (1,3)}}`. Adding a new effect here + strings in `combat_prose.py` is sufficient; no engine changes needed.
- `HUD_STATS`: which stats appear in the HUD
- `START_SCENE`: entry point scene key

**Content — `content/`**
- `enemies.py`: Enemy definitions. Each enemy is a dict with stats, phrases, loot, and optional `on_death` side effects (`flag`, `memory`). No engine changes needed to add enemies.
- `combat_prose.py`: All combat narrative strings (`STRINGS` dict) and prose helper functions (`light_prose`, `heavy_prose`, `damage_word`).
- `act1.py`, `act2.py`: Scene dicts per act. Pure data, no logic.
- `scenes.py`: Thin aggregator — `SCENES = {**ACT1, **ACT2}`

**Frontend — `static/js/game.js` + `audio.js`**
- Vanilla JS, no frameworks
- `game.js`: Fetches scenes/choices/combat from API, updates DOM, manages HUD
- `audio.js`: Scene-based music via `art_key` → track mapping; crossfade (2s); independent music/SFX volume

## Key Game Systems

- **Curse Accumulation**: Deaths add curse stacks, darkening prose and scaling enemy damage (`1.0 + curse_stacks * 0.06`)
- **Hidden Moral Stats**: honour, resolve, brutality, mercy affect choice availability and conditional prose variants
- **Memory Fragments**: Narrative collectibles visible in HUD
- **Echo Shards**: Combat currency for Runic Burst ability
- **Equipment slots**: `equipped` dict on PlayerState; `"weapon"`, `"shield"`, and `"body"` slots. Bear pelt (`body`) enables berserk mode (removes parry/mercy/flee).
- **Act progression**: Act I complete; Act II structurally complete; Act III placeholder; Act IV planned

## Content Authoring

### Adding a scene
Add an entry to `content/act1.py` or `content/act2.py` and register it in the local `SCENES` dict at the bottom of the file. Scene keys must be unique. Preceding scenes reference this key via `choices[n]["next"]` or `"next"`.

```python
SCENE_MY_SCENE = {
    "art": "art_key",          # maps to static/svg/<art_key>.png and audio
    "header": {"title": "...", "subtitle": "..."},  # optional
    "beats": [...],
    "choices": [...],          # omit for auto-advance via "next"
    "next": "next_scene_key",  # used if no choices, or after combat victory
}
```

### Beat types
| Type | Effect |
|------|--------|
| `prose` | Paragraph of narrative text |
| `italic` | Italicised prose (speech, sensation) |
| `memory` | Adds memory fragment; `key`, `label`, `text` |
| `conditional_prose` | Shows first matching `variants[].condition`. Optional `"type": "italic"` on a variant renders it italic. |
| `combat` | Triggers combat with `enemy` key; skipped if already defeated |
| `stat` | `{"changes": {"stat": delta}}` — first visit only. Use `{"echo_shards": N}` for shard rewards. |
| `flag` | Sets a story flag — first visit only |
| `item` | `action: "give"` or `action: "take"` — first visit only |
| `heal` | Restores HP — first visit only |
| `input` | Text input prompt |

### Condition DSL (used in `condition` fields on beats and choices)
```python
{"flag":     "name"}              # flag is set
{"memory":   "name"}              # player has memory
{"has_item": "name"}              # item in inventory
{"equipped": "weapon_name"}       # weapon slot matches
{"stat_gte": "stat", "value": N}  # stat >= N
{"not": <cond>}
{"and": [<cond>, ...]}
{"or":  [<cond>, ...]}
```

### Adding an enemy
Add an entry to `content/enemies.py`. The engine handles all combat mechanics generically.

```python
"my_enemy": {
    "name": "Full Name", "name_short": "Short",
    "hp": 60, "damage": (10, 20), "accuracy": 0.65,
    "shards": (80, 150),
    "loot": [("item_name", 0.8)],
    "on_death": {                        # optional
        "flag":   "my_flag",
        "memory": ("key", "label"),
    },
    "phrases": {"windup": [...], "hit": [...], "miss": [...], "death": [...]},
}
```

Optional combat feature flags: `shield` (reduces flanking), `drain`/`drain_amount` (sentinel mechanic), `phases` (boss phase count).

Optional `"weapon"` dict on enemy: `{"name": "...", "effect": "bleeding"}` — causes bleeding on the player when the enemy hits (4–8 dmg/turn for 3 turns, does not stack).

Optional `"variants"` dict: named stat overrides used when a scene specifies `"variant"`. Any field can be overridden (`hp`, `damage`, `accuracy`, `weapon`, etc.).

```python
"variants": {
    "frenzied": {"hp": 65, "damage": (12, 22), "accuracy": 0.70,
                 "weapon": {"name": "jagged axe", "effect": "bleeding"}},
    "wounded":  {"hp": 25, "damage": (6, 14)},
},
```

Trigger a variant from a scene beat:
```python
{"type": "combat", "enemy": "draugar_weak", "variant": "frenzied"}
```

Current enemies: `rat`, `wolf`, `hermit`, `draugar_weak`, `shieldwall_draugar`, `fog_sentinel`, `gunnar`. See `content/enemies.py` for full variant list per enemy.

### Adding equipment
Add an entry to `EQUIPMENT` in `content/game_config.py`. Auto-equip and stat lookups are handled generically.

```python
"my item": {"slot": "weapon", "tier": 2, "damage_bonus": 5},
"my item": {"slot": "weapon", "tier": 2, "damage_bonus": 5, "effect": "bleeding"},
"my shield": {"slot": "shield", "tier": 1, "defense": 4},
```

Optional `"effect"` on weapons: `"bleeding"` deals 4–8 damage/turn for 1–3 turns after a hit (does not stack). Enemy bleeds; player bleeds when hit by an enemy with a `"weapon"` carrying the same effect. Effect properties are defined in `EFFECTS` in `game_config.py`.

### Adding a status effect
Add an entry to `EFFECTS` in `content/game_config.py`:

```python
"poison": {"dmg": (2, 5), "duration": 4},      # static duration
"frostbite": {"dmg": (3, 6), "duration": (1, 4)},  # random duration
```

Add the corresponding string keys to `STRINGS` in `content/combat_prose.py`:

```python
"poison_open_enemy":  "Venom seeps into the wound.",
"poison_tick_enemy":  "{name} convulses — {dmg} damage.",
"poison_slow":        "The venom fades.",
"poison_open_player": "You feel the burn of venom.",
"poison_tick_player": "The poison burns — {dmg} damage.",
```

Apply the effect in content (enemy weapon) or engine code via `_apply_effect("poison", target_effects)`. No other engine changes needed.

### Art and audio
- Images: `static/svg/<art_key>.png`
- Music: add `"art_key": "track_name"` to `SCENE_MUSIC` in `static/js/audio.js`, place `track_name.mp3` in `static/audio/music/`
- The `"art"` field in a scene drives both the image and the music track
