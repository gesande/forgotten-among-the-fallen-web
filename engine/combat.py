# ============================================================
#  engine/combat.py
#  Text-based combat — all outcomes narrated as prose.
#  No HP bars. Damage is described. Stats shape what happens.
# ============================================================
import random
from engine.renderer import (
    print_prose, print_combat, print_damage, print_italic,
    print_separator, pause, ask_choice, print_system, C
)
from engine.graphics import art_death, art_combat

# ── Enemy templates ───────────────────────────────────────────
ENEMIES = {
    "draugar_weak": {
        "name":        "a Risen Footsoldier",
        "name_short":  "the Draugar",
        "hp":          40,
        "damage":      (8, 16),
        "accuracy":    0.60,
        "parry_chance":0.15,
        "phrases": {
            "windup":  [
                "It raises both rotting arms, a slow overhead swing telegraphed by its dead eyes.",
                "The thing lurches forward, arms wide — you can see the blow coming.",
                "It groans and swings wide, ice-slow.",
            ],
            "hit":     [
                "The axe catches you across the ribs. Something cracks.",
                "You are too slow. The blow lands against your shoulder.",
                "It finds a gap in your guard. The pain is distant, numbed by something older than pain.",
            ],
            "miss":    [
                "You step aside. The thing stumbles through its own momentum.",
                "It misses. The axe buries itself in the mud.",
                "You turn your body and the blow passes through air.",
            ],
            "death":   [
                "It collapses without a sound. Whatever held it upright is gone.",
                "The Draugar falls. Blue-grey mist rises from where it lands.",
                "It drops to the mud. The eyes dim — they were never truly lit.",
            ],
        },
        "loot": [("iron scraps", 0.7), ("echo dust", 0.9)],
        "shards": (60, 120),
    },
    "shieldwall_draugar": {
        "name":        "a Shieldwall Draugar",
        "name_short":  "the Shieldwall",
        "hp":          65,
        "damage":      (12, 20),
        "accuracy":    0.55,
        "parry_chance":0.25,
        "shield":      True,   # must be flanked first
        "flanked":     False,
        "phrases": {
            "windup":  [
                "It bashes its shield forward and swings behind the momentum.",
                "The creature advances in a tight guard stance. It knows how to fight.",
                "It shouts — a broken, wet sound — and the Draugar nearby begin to stir.",
            ],
            "hit":     [
                "You are caught. The iron rim of the shield hits first, then the blade.",
                "It punches through your guard. You taste iron.",
                "The blow is heavier than it should be. Your knees buckle.",
            ],
            "miss":    [
                "You roll under the arc. The Shieldwall cannot stop its own momentum.",
                "You circle left. It cannot turn fast enough.",
                "The strike grazes you — close, too close.",
            ],
            "death":   [
                "Without the shield raised, it was never a warrior. Just a body remembering war.",
                "It falls in pieces — the shield first, then it.",
                "The Shieldwall crumbles. The others nearby seem to notice.",
            ],
        },
        "loot": [("iron scraps", 1.0), ("cracked shield", 0.5)],
        "shards": (100, 180),
    },
    "gunnar": {
        "name":        "Gunnar the Hollow King",
        "name_short":  "Gunnar",
        "hp":          120,
        "damage":      (14, 28),
        "accuracy":    0.72,
        "parry_chance":0.30,
        "phases": 3,
        "current_phase": 1,
        "phrases": {
            "windup":  [
                "Gunnar steps back — and for a moment you see the man he was. Then the axe rises.",
                '"You remember," he says. He swings.',
                "He shifts his weight. Every movement is something you were taught. By him.",
            ],
            "hit":     [
                '"Still slow," he says, as the axe bites into your side.',
                "He catches you with the flat of the blade. Humiliating. Deliberate.",
                "You feel the blow before you see it. Muscle memory. His.",
            ],
            "miss":    [
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

def roll(sides: int) -> int:
    return random.randint(1, sides)

def roll_range(lo: int, hi: int) -> int:
    return random.randint(lo, hi)

def chance(prob: float) -> bool:
    return random.random() < prob

# ── Combat resolution ─────────────────────────────────────────

class CombatResult:
    def __init__(self):
        self.player_won:   bool = False
        self.player_fled:  bool = False
        self.player_died:  bool = False
        self.items_gained: list = []
        self.shards_gained:int  = 0

def run_combat(state, enemy_key: str) -> CombatResult:
    """
    Full combat loop — returns CombatResult.
    All HP changes are narrated; numbers stay hidden.
    """
    result = CombatResult()
    enemy  = dict(ENEMIES[enemy_key])  # copy so we don't mutate template
    enemy["current_hp"] = enemy["hp"]

    _combat_intro(enemy, state)

    round_num = 0
    while True:
        round_num += 1
        print_separator("thin")
        print()

        # ── Special phases ────────────────────────────────────
        if enemy.get("phases"):
            _check_phase(enemy, state)

        # ── Player turn ───────────────────────────────────────
        action = _player_turn(enemy, state)

        if action == "flee":
            result.player_fled = True
            _do_flee(state)
            break

        # Resolve player attack
        _resolve_player_attack(action, enemy, state)

        if enemy["current_hp"] <= 0:
            _enemy_death(enemy, state, result)
            result.player_won = True
            break

        # ── Enemy turn ────────────────────────────────────────
        pause("  [ brace yourself ]")
        _resolve_enemy_attack(enemy, state)

        # Taunt (boss only)
        if "taunt" in enemy.get("phrases", {}) and chance(0.4):
            taunt = random.choice(enemy["phrases"]["taunt"])
            print()
            print_italic(taunt)
            print()

        if state.is_dead():
            result.player_died = True
            _player_death(state)
            break

    return result

# ── Combat intro ──────────────────────────────────────────────

def _combat_intro(enemy: dict, state) -> None:
    print()
    art_combat(enemy.get("name", ""))
    print_separator("rune")
    print()
    pause(f"  {enemy['name']} blocks your path  ")

def _check_phase(enemy: dict, state) -> None:
    hp_ratio = enemy["current_hp"] / enemy["hp"]
    if enemy["current_phase"] == 1 and hp_ratio <= 0.65:
        enemy["current_phase"] = 2
        print()
        print_combat(enemy["phrases"].get("phase2", ""))
        print()
        pause()
    elif enemy["current_phase"] == 2 and hp_ratio <= 0.30:
        enemy["current_phase"] = 3
        print()
        print_combat(enemy["phrases"].get("phase3", ""))
        print()
        pause()

# ── Player turn ───────────────────────────────────────────────

def _player_turn(enemy: dict, state) -> str:
    choices = _build_player_choices(enemy, state)
    chosen  = ask_choice(choices, state)
    return chosen["action"]

def _build_player_choices(enemy: dict, state) -> list:
    hp_ratio = state.health / state.max_health
    choices  = []

    # Light attack — always available
    choices.append({
        "label":  "Strike — a fast, measured blow",
        "action": "light",
    })

    # Heavy — costs stamina, unlocked by resolve
    choices.append({
        "label":  "Commit — a heavy, reckless strike",
        "action": "heavy",
    })

    # Parry — requires honour or resolve
    choices.append({
        "label":  "Wait for the opening — attempt a parry",
        "action": "parry",
    })

    # Shield flank — only vs shielded enemies
    if enemy.get("shield") and not enemy.get("flanked"):
        choices.append({
            "label":  "Circle wide — find the flank",
            "action": "flank",
        })

    # Runic burst — requires shards
    if state.echo_shards >= 100:
        choices.append({
            "label":  "Spend shards — Runic Burst",
            "action": "runic",
        })

    # Mercy — only vs non-boss, low enemy HP
    if not enemy.get("phases") and enemy["current_hp"] < enemy["hp"] * 0.30:
        choices.append({
            "label":  "Lower your weapon",
            "action": "mercy",
            "condition": lambda s: s.honour >= 40,
        })

    # Flee — always possible, costs health
    choices.append({
        "label":  "Retreat into the fog",
        "action": "flee",
    })

    return choices

# ── Resolve player attack ─────────────────────────────────────

def _resolve_player_attack(action: str, enemy: dict, state) -> None:
    print()

    if action == "light":
        base = roll_range(8, 18)
        dmg  = _apply_modifiers(base, state, "light")
        _hit_enemy(dmg, enemy)
        print_combat(_light_attack_prose(dmg, enemy))

    elif action == "heavy":
        if chance(0.25):  # heavy attacks can miss
            print_combat("You overcommit. The blow goes wide and you nearly lose your footing.")
            state.modify_stat("stamina", -15)
        else:
            base = roll_range(18, 30)
            dmg  = _apply_modifiers(base, state, "heavy")
            _hit_enemy(dmg, enemy)
            print_combat(_heavy_attack_prose(dmg, enemy))

    elif action == "parry":
        if chance(0.45 + state.honour * 0.003):
            dmg = roll_range(12, 22)
            _hit_enemy(dmg, enemy)
            state.modify_stat("honour", 2)
            print_combat("You read the blow perfectly. Your parry opens a gap — you answer it.")
            print_combat(f"{enemy['name_short']} staggers. Your strike finds bone.")
        else:
            print_combat("The parry fails. You mistimed it. The blow is coming — you brace.")
            dmg = roll_range(*enemy["damage"]) // 2
            actual = state.take_damage(dmg)
            print_damage(f"It costs you. You absorb {_damage_word(actual)}.")

    elif action == "flank":
        enemy["flanked"] = True
        print_combat("You circle wide, drawing its attention, then break right. It cannot pivot in time.")
        print_combat("The shield is useless now. Its side is open.")

    elif action == "runic":
        state.echo_shards -= 100
        dmg = roll_range(35, 50)
        _hit_enemy(dmg, enemy)
        print_combat("The shards burn cold in your fist. The rune ᚠ blooms across your weapon.")
        print_combat(f"The burst hits {enemy['name_short']} like a memory of fire.")
        state.modify_stat("brutality", 5)

    elif action == "mercy":
        # Only possible vs non-boss at low HP
        enemy["current_hp"] = 0
        state.modify_stat("mercy", 10)
        state.modify_stat("honour", 5)
        print_combat("You lower your weapon. It looks at you — confused, perhaps. Grateful, possibly.")
        print_combat("The Draugar sinks to the ground. It does not rise. Not as a threat.")

# ── Resolve enemy attack ──────────────────────────────────────

def _resolve_enemy_attack(enemy: dict, state) -> None:
    # Windup telegraph
    windup = random.choice(enemy["phrases"]["windup"])
    print_combat(windup)
    print()

    # Shielded enemies deal more if not flanked
    dmg_range = enemy["damage"]
    if enemy.get("shield") and not enemy.get("flanked"):
        dmg_range = (dmg_range[0] + 5, dmg_range[1] + 8)

    if chance(enemy["accuracy"]):
        base   = roll_range(*dmg_range)
        # Curse makes enemies hit harder
        scaled = int(base * (1 + state.curse_stacks * 0.06))
        actual = state.take_damage(scaled)
        phrase = random.choice(enemy["phrases"]["hit"])
        print_damage(phrase)
        print_damage(f"  — {_damage_word(actual)} taken.")
    else:
        phrase = random.choice(enemy["phrases"]["miss"])
        print_combat(phrase)

# ── Enemy death ───────────────────────────────────────────────

def _enemy_death(enemy: dict, state, result: CombatResult) -> None:
    print()
    phrase = random.choice(enemy["phrases"]["death"])
    print_combat(phrase)
    print()

    # Shards
    lo, hi = enemy["shards"]
    shards  = roll_range(lo, hi)
    state.echo_shards += shards
    result.shards_gained = shards
    print_system(f"  + {shards} echo shards")

    # Loot
    for item, prob in enemy.get("loot", []):
        if chance(prob):
            state.add_item(item)
            result.items_gained.append(item)
            print_system(f"  + {item}")
    print()

# ── Flee ──────────────────────────────────────────────────────

def _do_flee(state) -> None:
    dmg = roll_range(10, 20)
    state.take_damage(dmg)
    print()
    print_combat("You run. The thing behind you is slower — but not by much.")
    print_combat("You reach the fog. It doesn't follow. It never follows into the fog.")
    print_damage(f"You are {_damage_word(dmg)} from the retreat.")
    state.modify_stat("honour", -5)

# ── Player death ──────────────────────────────────────────────

def _player_death(state) -> None:
    art_death()
    print()
    print_damage("You fall.")
    print()
    print_combat("Not death — you have already done that. But the battlefield takes you again.")
    print_combat("When you wake, it will be at the Bone Cairn. The shards will be gone.")
    print_combat("The dead will be standing. Something will be different — darker — in the fog.")
    print()
    state.deaths     += 1
    state.curse_stacks = min(5, state.curse_stacks + 1)
    state.echo_shards  = state.echo_shards // 4
    state.health       = state.max_health
    pause("  [ the world resets ]")

# ── Helpers ───────────────────────────────────────────────────

def _hit_enemy(dmg: int, enemy: dict) -> None:
    enemy["current_hp"] = max(0, enemy["current_hp"] - dmg)

def _apply_modifiers(base: int, state, attack_type: str) -> int:
    mod = base
    if state.brutality > 50:
        mod += roll(6)
    if state.honour > 70 and attack_type == "light":
        mod += roll(4)
    if state.is_cursed():
        mod -= roll(4)
    return max(1, mod)

def _damage_word(dmg: int) -> str:
    if dmg <= 5:   return "a graze"
    if dmg <= 12:  return "a wound"
    if dmg <= 20:  return "a serious wound"
    if dmg <= 30:  return "a grievous blow"
    return "something that would kill a living man"

def _light_attack_prose(dmg: int, enemy: dict) -> str:
    name = enemy["name_short"]
    if dmg < 10:
        return f"Your blow glances off {name}. It slows, but does not stop."
    if dmg < 20:
        return f"The strike lands clean. {name} staggers."
    return f"You drive the blow deep. {name} reels."

def _heavy_attack_prose(dmg: int, enemy: dict) -> str:
    name = enemy["name_short"]
    if dmg < 15:
        return f"A solid hit — the weight tells, even if the precision does not."
    if dmg < 25:
        return f"{name} is staggered by the force. You feel the impact in your shoulders."
    return f"The heavy strike connects. {name} is driven back — something in it is broken."
