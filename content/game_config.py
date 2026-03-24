# ============================================================
#  content/game_config.py
#  Game-specific configuration consumed by the engine.
#  Replace this file to define a different game.
# ============================================================

# ── Stat definitions ──────────────────────────────────────────
# All stats the engine should know about (used for bounds in
# modify_stat). Stats not listed here default to 0–100 clamping.
STATS = {
    "honour":       {"default": 50,  "min": 0, "max": 100},
    "resolve":      {"default": 50,  "min": 0, "max": 100},
    "brutality":    {"default": 0,   "min": 0, "max": 100},
    "mercy":        {"default": 0,   "min": 0, "max": 100},
    "wrath":        {"default": 0,   "min": 0, "max": 100},
    "stamina":      {"default": 100, "min": 0, "max": 100},
    "echo_shards":  {"default": 0,   "min": 0, "max": None},
    "curse_stacks": {"default": 0,   "min": 0, "max": 5},
}

# ── Weapon auto-equip tiers ────────────────────────────────────
# Higher tier weapons are auto-equipped when picked up.
WEAPON_TIERS = {
    "bare hands":   0,
    "rusted axe":   1,
    "Leif's knife": 2,
    "Gunnar's Axe": 3,
}

# ── HUD layout ────────────────────────────────────────────────
# Maps frontend HUD keys to stat names on PlayerState.
# "max_stat" is optional; when present, also outputs max_{key}.
HUD_STATS = [
    {"key": "wrath",  "stat": "wrath",        "max_stat": "max_wrath"},
    {"key": "curse",  "stat": "curse_stacks"},
    {"key": "shards", "stat": "echo_shards"},
]

# ── Starting scene ─────────────────────────────────────────────
START_SCENE = "name_entry"
