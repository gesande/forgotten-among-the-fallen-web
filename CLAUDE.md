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

There are no tests, linting, or build tools configured.

## Architecture

**Backend (Python/Flask) — `app.py`**
- Stateless HTTP server; player state lives in Flask session (not database)
- State serialized/deserialized as `PlayerState` dataclass on every request
- API routes: `/api/new`, `/api/load`, `/api/scene`, `/api/choose`, `/api/combat/action`, `/api/advance`, `/api/status`

**Game Engine — `engine/`**
- `state.py`: `PlayerState` dataclass — visible resources (health, stamina, wrath, echo_shards, curse_stacks), hidden moral stats (honour, resolve, brutality, mercy, 0–100), inventory, story flags, memory fragments. Saves/loads to `saves/save_0.json`.
- `scene_web.py`: Processes scene beats (prose, choices, stat changes, flags, items, combat triggers) and returns JSON. Side effects apply only on first scene visit. Auto-advances scenes with no prose/choices/combat.
- `combat_web.py`: Turn-based combat engine. Player actions: light/heavy strike, parry, flank, runic burst, mercy, flee. Curse stacks scale enemy damage via `1.0 + curse_stacks * 0.06`.

**Content — `content/scenes.py`**
- ~2974 lines of pure Python dicts — no logic, only declarative scene data
- 58 scenes across Act I — The Battlefield of Silence (28 scenes: awakening → Leif → battlefield hub → Gunnar boss → `act1_end`) and Act II — The Stirring Beneath (30 scenes: fog road → Held → Sentinel → Gatehouse → Great Hall / Odrik)
- Beat types: `prose`, `italic`, `memory`, `conditional_prose`, `combat`, `stat`, `flag`, `item`, `input`
- Scenes reference enemies by key (e.g. `"draugar_weak"`, `"gunnar"`) — resolved in `combat_web.py`

**Frontend — `static/js/game.js` + `audio.js`**
- Vanilla JS, no frameworks
- `game.js`: Fetches scenes/choices/combat from API, updates DOM, manages HUD and loading states
- `audio.js`: Scene-based music via `art_key` → track mapping; crossfade (2s); independent music/SFX volume

## Key Game Systems

- **Curse Accumulation**: Deaths add curse stacks, darkening prose and scaling enemy damage
- **Hidden Moral Stats**: honour, resolve, brutality, mercy affect choice availability and conditional prose variants
- **Memory Fragments**: Narrative collectibles; visible in HUD
- **Echo Shards**: Combat currency for Runic Burst ability
- **Act progression**: Act I complete and playtestable; Act II drafted; Acts III/IV planned

## Content Authoring

To add a new scene, add an entry to the `SCENES` dict in `content/scenes.py` following existing patterns. Scene keys must be unique and referenced by `choices[n]["next"]` from preceding scenes. New enemy types are defined in `combat_web.py` in the `ENEMIES` dict.

Art assets follow a naming convention: `static/svg/<scene_key>.png` (PNG for display) with optional `.svg` source. Audio tracks in `static/audio/music/` are mapped in `audio.js`.
