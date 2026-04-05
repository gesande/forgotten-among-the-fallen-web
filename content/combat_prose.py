# ============================================================
#  content/combat_prose.py
#  All game-specific prose strings for the combat engine.
#  Replace this file to change the narrative voice of combat.
# ============================================================

# ── Static strings ─────────────────────────────────────────────
STRINGS = {
    "start_combat": "You face {name}.",
    "overcommit": "You overcommit. The blow goes wide and you nearly lose your footing.",
    "parry_success_1": "You read the blow perfectly. Your parry opens a gap — you answer it.",
    "parry_success_2": "{name} staggers. Your strike finds bone.",
    "parry_fail_1": "The parry fails. You mistimed it.",
    "parry_fail_2": "It costs you — {damage}.",
    "flank": "You circle wide. The shield is useless now. Its side is open.",
    "runic_windup": "The shards burn cold in your fist. The rune ᚠ blooms across your weapon.",
    "runic_hit": "The burst hits {name} like a memory of fire.",
    "runic_miss": "The runic force tears open air. The shards are gone.",
    "mercy": "You lower your weapon. It sinks to the ground. It does not rise.",
    "flee_1": "You run. The thing behind you is slower — but not by much.",
    "flee_2": "You reach the fog. It doesn't follow into the fog.",
    "flee_cost": "You are {damage} from the retreat.",
    "player_death_1": "You fall.",
    "player_death_2": "When you wake, it will be at the Bone Cairn.",
    "bleeding_open_enemy": "The wound opens. Dark blood begins to run.",
    "bleeding_tick_enemy": "The wound bleeds. {name} loses {dmg}.",
    "bleeding_slow": "The bleeding slows.",
    "bleeding_open_player": "The wound opens. You are bleeding.",
    "bleeding_tick_player": "Your wound bleeds — {dmg} damage.",
    "near_death": "Something gives way in you. Not bone — something deeper.",
    "phase_resolve_loss": "The sight of it shakes you. Whatever it is, it is not done.",
}


# ── Damage description ─────────────────────────────────────────
def damage_word(dmg: int) -> str:
    if dmg <= 5:
        return "a graze"
    if dmg <= 12:
        return "a wound"
    if dmg <= 20:
        return "a serious wound"
    if dmg <= 30:
        return "a grievous blow"
    return "something that would kill a living man"


# ── Hit prose ──────────────────────────────────────────────────
def light_prose(dmg: int, enemy_name: str) -> str:
    if dmg < 10:
        return f"Your blow glances off {enemy_name}. It slows, but does not stop."
    if dmg < 20:
        return f"The strike lands clean. {enemy_name} staggers."
    return f"You drive the blow deep. {enemy_name} reels."


def heavy_prose(dmg: int, enemy_name: str) -> str:
    if dmg < 15:
        return "A solid hit — the weight tells, even if the precision does not."
    if dmg < 25:
        return (
            f"{enemy_name} is staggered by the force. "
            "You feel the impact in your shoulders."
        )
    return (
        f"The heavy strike connects. {enemy_name} is driven back "
        "— something in it is broken."
    )
