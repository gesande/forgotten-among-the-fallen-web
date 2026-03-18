# ============================================================
#  engine/combat_web.py
#  Combat engine for the web version.
#  Returns structured dicts instead of printing to terminal.
#  All prose, choices, and outcomes go through JSON to the UI.
# ============================================================
import random
from engine.state import PlayerState

ENEMIES = {
    "draugar_weak": {
        "name":        "a Risen Footsoldier",
        "name_short":  "the Draugar",
        "hp":          40,
        "damage":      (8, 16),
        "accuracy":    0.60,
        "phrases": {
            "windup": [
                "It raises both rotting arms, a slow overhead swing telegraphed by its dead eyes.",
                "The thing lurches forward, arms wide — you can see the blow coming.",
                "It groans and swings wide, ice-slow.",
            ],
            "hit": [
                "The axe catches you across the ribs. Something cracks.",
                "You are too slow. The blow lands against your shoulder.",
                "It finds a gap in your guard. The pain is distant, numbed by something older than pain.",
            ],
            "miss": [
                "You step aside. The thing stumbles through its own momentum.",
                "It misses. The axe buries itself in the mud.",
                "You turn your body and the blow passes through air.",
            ],
            "death": [
                "It collapses without a sound. Whatever held it upright is gone.",
                "The Draugar falls. Blue-grey mist rises from where it lands.",
                "It drops to the mud. The eyes dim — they were never truly lit.",
            ],
        },
        "loot":   [("iron scraps", 0.7), ("echo dust", 0.9)],
        "shards": (60, 120),
    },
    "shieldwall_draugar": {
        "name":        "a Shieldwall Draugar",
        "name_short":  "the Shieldwall",
        "hp":          65,
        "damage":      (12, 20),
        "accuracy":    0.55,
        "shield":      True,
        "flanked":     False,
        "phrases": {
            "windup": [
                "It bashes its shield forward and swings behind the momentum.",
                "The creature advances in a tight guard stance. It knows how to fight.",
                "It shouts — a broken, wet sound — and the Draugar nearby begin to stir.",
            ],
            "hit": [
                "You are caught. The iron rim of the shield hits first, then the blade.",
                "It punches through your guard. You taste iron.",
                "The blow is heavier than it should be. Your knees buckle.",
            ],
            "miss": [
                "You roll under the arc. The Shieldwall cannot stop its own momentum.",
                "You circle left. It cannot turn fast enough.",
                "The strike grazes you — close, too close.",
            ],
            "death": [
                "Without the shield raised, it was never a warrior. Just a body remembering war.",
                "It falls in pieces — the shield first, then it.",
                "The Shieldwall crumbles. The others nearby seem to notice.",
            ],
        },
        "loot":   [("iron scraps", 1.0), ("cracked shield", 0.5)],
        "shards": (100, 180),
    },
    "gunnar": {
        "name":        "Gunnar the Hollow King",
        "name_short":  "Gunnar",
        "hp":          120,
        "damage":      (14, 28),
        "accuracy":    0.72,
        "phases":      3,
        "current_phase": 1,
        "phrases": {
            "windup": [
                "Gunnar steps back — and for a moment you see the man he was. Then the axe rises.",
                '"You remember," he says. He swings.',
                "He shifts his weight. Every movement is something you were taught. By him.",
            ],
            "hit": [
                '"Still slow," he says, as the axe bites into your side.',
                "He catches you with the flat of the blade. Humiliating. Deliberate.",
                "You feel the blow before you see it. Muscle memory. His.",
            ],
            "miss": [
                "You remember this. You have drilled against this exact strike a hundred times.",
                "You parry — and for a moment, he looks almost proud.",
                "You step inside his reach. He was not expecting that. Neither were you.",
            ],
            "taunt": [
                '"You broke your oath. Odin does not forget."',
                '"I remember what you did. Do you?"',
                '"Fight me like you mean it. Fight me like that night."',
                '"Why do you think the Valkyries never came?"',
            ],
            "phase2":  "Gunnar roars — a sound that is not grief, not rage, but something between them. The air around him darkens.",
            "phase3":  "He speaks a word in Old Norse you do not recognise. His shadow splits. There are two of him now — one still, one moving.",
            "death":   '"It... does not matter," he says. "You will wake. And I will be here. I am always here."',
        },
        "loot":   [("Remembrance Key", 1.0), ("Gunnar's Axe", 1.0)],
        "shards": (2400, 2400),
    },
}

# ── Dice ──────────────────────────────────────────────────────
def roll(sides):        return random.randint(1, sides)
def roll_range(lo, hi): return random.randint(lo, hi)
def chance(p):          return random.random() < p

def damage_word(dmg):
    if dmg <= 5:   return "a graze"
    if dmg <= 12:  return "a wound"
    if dmg <= 20:  return "a serious wound"
    if dmg <= 30:  return "a grievous blow"
    return "something that would kill a living man"

# ── Combat state lives in Flask session ───────────────────────
# combat_state = { "enemy": {...}, "log": [...], "over": bool, "won": bool }

def start_combat(enemy_key: str, player: PlayerState) -> dict:
    e = dict(ENEMIES[enemy_key])
    e["current_hp"] = e["hp"]
    e["key"]        = enemy_key
    # Apply curse scaling
    scale = 1.0 + player.curse_stacks * 0.06
    e["damage"] = (int(e["damage"][0] * scale), int(e["damage"][1] * scale))
    return {
        "enemy":    e,
        "log":      [f"You face {e['name']}."],
        "over":     False,
        "won":      False,
        "fled":     False,
        "shards_gained": 0,
        "items_gained":  [],
    }

def get_player_actions(combat_state: dict, player: PlayerState) -> list:
    e = combat_state["enemy"]
    actions = [
        {"id": "light",  "label": "Strike — a fast, measured blow"},
        {"id": "heavy",  "label": "Commit — a heavy, reckless strike"},
        {"id": "parry",  "label": "Wait for the opening — attempt a parry"},
    ]
    if e.get("shield") and not e.get("flanked"):
        actions.append({"id": "flank", "label": "Circle wide — find the flank"})
    if player.echo_shards >= 100:
        actions.append({"id": "runic", "label": f"Spend 100 shards — Runic Burst"})
    if not e.get("phases") and e["current_hp"] < e["hp"] * 0.30 and player.honour >= 40:
        actions.append({"id": "mercy", "label": "Lower your weapon"})
    actions.append({"id": "flee", "label": "Retreat into the fog"})
    return actions

def resolve_action(action_id: str, combat_state: dict, player: PlayerState) -> dict:
    """Process one player action + enemy counter. Returns updated combat_state."""
    e   = combat_state["enemy"]
    log = combat_state["log"]

    # ── Player action ─────────────────────────────────────────
    if action_id == "light":
        base = roll_range(8, 18)
        dmg  = _apply_mods(base, player, "light")
        _hit_enemy(dmg, e)
        player.modify_stat("wrath", 10)
        combo = player.flags.get("combo", 0) + 1
        player.set_flag("combo", min(combo, 3))
        log.append(_light_prose(dmg, e))

    elif action_id == "heavy":
        if chance(0.25):
            log.append("You overcommit. The blow goes wide and you nearly lose your footing.")
        else:
            base = roll_range(18, 30)
            dmg  = _apply_mods(base, player, "heavy")
            _hit_enemy(dmg, e)
            player.modify_stat("wrath", 18)
            log.append(_heavy_prose(dmg, e))

    elif action_id == "parry":
        if chance(0.45 + player.honour * 0.003):
            dmg = roll_range(12, 22)
            _hit_enemy(dmg, e)
            player.modify_stat("honour", 2)
            player.modify_stat("wrath", 25)
            log.append("You read the blow perfectly. Your parry opens a gap — you answer it.")
            log.append(f"{e['name_short']} staggers. Your strike finds bone.")
        else:
            dmg    = roll_range(*e["damage"]) // 2
            actual = player.take_damage(dmg)
            log.append("The parry fails. You mistimed it.")
            log.append(f"It costs you — {damage_word(actual)}.")

    elif action_id == "flank":
        e["flanked"] = True
        log.append("You circle wide. The shield is useless now. Its side is open.")

    elif action_id == "runic":
        player.echo_shards -= 100
        dmg = roll_range(35, 50)
        _hit_enemy(dmg, e)
        player.modify_stat("brutality", 5)
        player.wrath = 0
        log.append("The shards burn cold in your fist. The rune ᚠ blooms across your weapon.")
        log.append(f"The burst hits {e['name_short']} like a memory of fire.")

    elif action_id == "mercy":
        e["current_hp"] = 0
        player.modify_stat("mercy", 10)
        player.modify_stat("honour", 5)
        log.append("You lower your weapon. It sinks to the ground. It does not rise.")

    elif action_id == "flee":
        dmg = roll_range(10, 20)
        player.take_damage(dmg)
        player.modify_stat("honour", -5)
        log.append("You run. The thing behind you is slower — but not by much.")
        log.append("You reach the fog. It doesn't follow into the fog.")
        log.append(f"You are {damage_word(dmg)} from the retreat.")
        combat_state["fled"] = True
        combat_state["over"] = True
        return combat_state

    # ── Check enemy death ─────────────────────────────────────
    if e["current_hp"] <= 0:
        _resolve_enemy_death(e, player, combat_state, log)
        combat_state["over"] = True
        combat_state["won"]  = True
        return combat_state

    # ── Phase transitions (boss) ──────────────────────────────
    if e.get("phases"):
        ratio = e["current_hp"] / e["hp"]
        if e["current_phase"] == 1 and ratio <= 0.65:
            e["current_phase"] = 2
            log.append(e["phrases"].get("phase2", ""))
        elif e["current_phase"] == 2 and ratio <= 0.30:
            e["current_phase"] = 3
            log.append(e["phrases"].get("phase3", ""))

    # ── Enemy turn ────────────────────────────────────────────
    if not combat_state["over"]:
        _resolve_enemy_turn(e, player, log)

    # Taunt
    if "taunt" in e.get("phrases", {}) and chance(0.35):
        log.append(random.choice(e["phrases"]["taunt"]))

    # Check player death
    if player.is_dead():
        log.append("You fall.")
        log.append("When you wake, it will be at the Bone Cairn.")
        player.deaths      += 1
        player.curse_stacks = min(5, player.curse_stacks + 1)
        player.echo_shards  = player.echo_shards // 4
        player.health       = player.max_health
        combat_state["over"]  = True
        combat_state["died"]  = True

    return combat_state

def _resolve_enemy_turn(e, player, log):
    windup = random.choice(e["phrases"]["windup"])
    log.append(windup)
    dmg_range = e["damage"]
    if e.get("shield") and not e.get("flanked"):
        dmg_range = (dmg_range[0] + 5, dmg_range[1] + 8)
    if chance(e["accuracy"]):
        dmg    = roll_range(*dmg_range)
        actual = player.take_damage(dmg)
        player.modify_stat("wrath", 8)
        log.append(random.choice(e["phrases"]["hit"]))
        log.append(f"— {damage_word(actual)} taken.")
    else:
        log.append(random.choice(e["phrases"]["miss"]))

def _resolve_enemy_death(e, player, combat_state, log):
    log.append(random.choice(e["phrases"]["death"]))
    lo, hi = e["shards"]
    shards  = roll_range(lo, hi)
    player.echo_shards += shards
    combat_state["shards_gained"] = shards
    for item, prob in e.get("loot", []):
        if chance(prob):
            player.add_item(item)
            combat_state["items_gained"].append(item)
    if e["key"] == "gunnar":
        player.add_memory("gunnar_defeated", "The death of Gunnar the Hollow King")
    player.set_flag(f"defeated_{e['key']}", True)

def _hit_enemy(dmg, e):
    e["current_hp"] = max(0, e["current_hp"] - dmg)

def _apply_mods(base, player, kind):
    mod = base
    if player.brutality > 50: mod += roll(6)
    if player.honour > 70 and kind == "light": mod += roll(4)
    if player.is_cursed(): mod -= roll(4)
    return max(1, mod)

def _light_prose(dmg, e):
    name = e["name_short"]
    if dmg < 10: return f"Your blow glances off {name}. It slows, but does not stop."
    if dmg < 20: return f"The strike lands clean. {name} staggers."
    return f"You drive the blow deep. {name} reels."

def _heavy_prose(dmg, e):
    name = e["name_short"]
    if dmg < 15: return f"A solid hit — the weight tells, even if the precision does not."
    if dmg < 25: return f"{name} is staggered by the force. You feel the impact in your shoulders."
    return f"The heavy strike connects. {name} is driven back — something in it is broken."
