# ============================================================
#  content/game_config.py
#  Game-specific configuration consumed by the engine.
#  Replace this file to define a different game.
# ============================================================

# ── Stat definitions ──────────────────────────────────────────
# All stats the engine should know about (used for bounds in
# modify_stat). Stats not listed here default to 0–100 clamping.
STATS = {
    "honour": {"default": 50, "min": 0, "max": 100, "threshold": 70},  # is_honoured >=
    "resolve": {"default": 50, "min": 0, "max": 100, "threshold": 20},  # is_broken   <
    "brutality": {
        "default": 0,
        "min": 0,
        "max": 100,
        "threshold": 60,
    },  # is_brutal   >=
    "mercy": {"default": 0, "min": 0, "max": 100},
    "wrath": {"default": 0, "min": 0, "max": 100},
    "stamina": {"default": 100, "min": 0, "max": 100},
    "echo_shards": {"default": 0, "min": 0, "max": None},
    "curse_stacks": {
        "default": 0,
        "min": 0,
        "max": 5,
        "threshold": 3,
    },  # is_cursed   >=
}

# ── Equipment registry ─────────────────────────────────────────
# All equippable items. "slot" determines which equipped[slot] they fill.
# Higher "tier" items auto-equip when picked up, replacing lower tier.
# Slot-specific properties:
#   weapon → "damage_bonus": flat added to every strike
#   shield → "defense":      flat damage absorbed per incoming hit
EQUIPMENT = {
    "bare hands": {"slot": "weapon", "tier": 0, "damage_bonus": 0},
    "rusted axe": {"slot": "weapon", "tier": 1, "damage_bonus": 0},
    "sharpened axe": {
        "slot": "weapon",
        "tier": 2,
        "damage_bonus": 4,
        "effect": "bleeding",
    },
    "Leif's knife": {"slot": "weapon", "tier": 2, "damage_bonus": 3},
    "Gunnar's Axe": {
        "slot": "weapon",
        "tier": 3,
        "damage_bonus": 8,
        "effect": "bleeding",
    },
    "traveller's shield": {"slot": "shield", "tier": 1, "defense": 4},
    # Body slot — pelts
    "wolf pelt": {"slot": "body", "tier": 1, "damage_bonus": 3},
    "bear pelt": {"slot": "body", "tier": 2, "damage_bonus": 5, "berserk": True},
}

# ── HUD layout ────────────────────────────────────────────────
# Maps frontend HUD keys to stat names on PlayerState.
# "max_stat" is optional; when present, also outputs max_{key}.
HUD_STATS = [
    {"key": "wrath", "stat": "wrath", "max_stat": "max_wrath"},
    {"key": "curse", "stat": "curse_stacks"},
    {"key": "shards", "stat": "echo_shards"},
]

# ── Starting scene ─────────────────────────────────────────────
START_SCENE = "name_entry"
