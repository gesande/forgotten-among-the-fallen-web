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

# ── Combat damage modifiers ───────────────────────────────────
# Applied in _apply_mods after equipment bonuses.
# Each entry: stat/fn check → bonus_die or penalty_die added to roll.
#   stat + gt:       getattr(player, stat) > gt
#   fn:              getattr(player, fn)() is truthy
#   action (opt):    only applies when action kind matches
COMBAT_MODS = [
    {"stat": "brutality", "gt": 50, "bonus_die": 6},
    {"stat": "honour", "gt": 70, "action": "light", "bonus_die": 4},
    {"fn": "is_cursed", "penalty_die": 4},
]

# ── Combat configuration ──────────────────────────────────────
# All numeric constants consumed by engine/combat.py.
COMBAT_CONFIG = {
    # Action damage ranges (lo, hi)
    "light_dmg": (8, 18),
    "heavy_dmg": (18, 30),
    "runic_dmg": (35, 50),
    "parry_counter_dmg": (12, 22),
    "flee_dmg": (10, 20),
    # Action chances
    "heavy_overcommit_chance": 0.25,
    "parry_base_chance": 0.45,
    "parry_honour_scale": 0.003,
    # Runic burst
    "runic_cost": 100,
    # Wrath gains
    "wrath_light": 10,
    "wrath_heavy": 18,
    "wrath_parry": 25,
    "wrath_hit_by_enemy": 8,
    # Mercy availability
    "mercy_honour_min": 40,
    "mercy_enemy_hp_ratio": 0.30,
    # Stat changes from actions
    "parry_honour_gain": 2,
    "mercy_mercy_gain": 10,
    "mercy_honour_gain": 5,
    "flee_honour_loss": -5,
    "runic_brutality_gain": 5,
    # Death
    "death_shard_divisor": 4,
    # Curse scaling (damage multiplier per stack)
    "curse_damage_scale": 0.06,
    # Boss phase HP thresholds
    "phase2_hp_ratio": 0.65,
    "phase3_hp_ratio": 0.30,
    # Shielded enemy bonus incoming damage
    "shield_enemy_dmg_bonus": (5, 8),
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
