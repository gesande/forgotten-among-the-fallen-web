# ============================================================
#  engine/combat.py
#  Combat engine — no game-specific prose or stat assumptions.
#  All narrative text lives in content/combat_prose.py.
#  All stat modifiers live in content/game_config.py COMBAT_MODS.
# ============================================================
import random
from engine.state import PlayerState
from engine.dice import roll, roll_range, chance
from content.game_config import EQUIPMENT, COMBAT_MODS, COMBAT_CONFIG
from content.enemies import ENEMIES
from content.combat_prose import (
    STRINGS,
    damage_word,
    light_prose,
    heavy_prose,
)

CC = COMBAT_CONFIG          # shorthand
A = CC["actions"]           # per-action config
S = STRINGS                 # shorthand


# ── Combat state lives in Flask session ───────────────────────
# combat_state = { "enemy": {...}, "log": [...], "over": bool, "won": bool }


def start_combat(
    enemy_key: str, player: PlayerState, variant: str | None = None
) -> dict:
    e = dict(ENEMIES[enemy_key])
    if variant:
        e.update(ENEMIES[enemy_key].get("variants", {}).get(variant, {}))
    e["current_hp"] = e["hp"]
    e["key"] = enemy_key
    e["effects"] = {}
    scale = 1.0 + player.curse_stacks * CC["curse_damage_scale"]
    e["damage"] = (int(e["damage"][0] * scale), int(e["damage"][1] * scale))
    return {
        "enemy": e,
        "log": [S["start_combat"].format(name=e["name"])],
        "over": False,
        "won": False,
        "fled": False,
        "shards_gained": 0,
        "items_gained": [],
        "player_effects": {},
    }


def get_player_actions(combat_state: dict, player: PlayerState) -> list:
    e = combat_state["enemy"]
    body_eq = EQUIPMENT.get(player.equipped.get("body", ""), {})
    berserk = body_eq.get("berserk", False)
    actions = [
        {"id": "light", "label": A["light"]["label"]},
        {"id": "heavy", "label": A["heavy"]["label"]},
    ]
    if not berserk:
        actions.append({"id": "parry", "label": A["parry"]["label"]})
    if e.get("shield") and not e.get("flanked"):
        actions.append({"id": "flank", "label": A["flank"]["label"]})
    if player.echo_shards >= A["runic"]["cost"]:
        actions.append({"id": "runic", "label": A["runic"]["label"]})
    if not berserk:
        mercy = A["mercy"]
        if (
            not e.get("phases")
            and e["current_hp"] < e["hp"] * mercy["enemy_hp_ratio"]
            and player.honour >= mercy["honour_min"]
        ):
            actions.append({"id": "mercy", "label": mercy["label"]})
        actions.append({"id": "flee", "label": A["flee"]["label"]})
    return actions


def resolve_action(action_id: str, combat_state: dict, player: PlayerState) -> dict:
    """Process one player action + enemy counter. Returns updated combat_state."""
    e = combat_state["enemy"]
    log = combat_state["log"]

    # ── Player effects tick (at turn start) ───────────────────
    _tick_player_effects(combat_state, player, log)
    if player.is_dead():
        return _handle_player_death(player, combat_state, log)

    # ── Player action ─────────────────────────────────────────
    if action_id == "light":
        base = roll_range(*A["light"]["dmg"])
        dmg = _apply_mods(base, player, "light")
        if _player_strikes(dmg, e, player, log):
            player.modify_stat("wrath", A["light"]["wrath"])
            combo = player.flags.get("combo", 0) + 1
            player.set_flag("combo", min(combo, 3))
            log.append(light_prose(dmg, e["name_short"]))

    elif action_id == "heavy":
        if chance(A["heavy"]["overcommit_chance"]):
            log.append(S["overcommit"])
        else:
            base = roll_range(*A["heavy"]["dmg"])
            dmg = _apply_mods(base, player, "heavy")
            if _player_strikes(dmg, e, player, log):
                player.modify_stat("wrath", A["heavy"]["wrath"])
                log.append(heavy_prose(dmg, e["name_short"]))

    elif action_id == "parry":
        p = A["parry"]
        if chance(p["base_chance"] + player.honour * p["honour_scale"]):
            dmg = roll_range(*p["dmg"])
            _hit_enemy(dmg, e, player, log)
            player.modify_stat("honour", p["honour_gain"])
            player.modify_stat("wrath", p["wrath"])
            log.append(S["parry_success_1"])
            log.append(S["parry_success_2"].format(name=e["name_short"]))
        else:
            dmg = roll_range(*e["damage"]) // 2
            actual = player.take_damage(dmg)
            log.append(S["parry_fail_1"])
            log.append(S["parry_fail_2"].format(damage=damage_word(actual)))

    elif action_id == "flank":
        e["flanked"] = True
        log.append(S["flank"])

    elif action_id == "runic":
        r = A["runic"]
        player.echo_shards -= r["cost"]
        dmg = roll_range(*r["dmg"])
        log.append(S["runic_windup"])
        if _player_strikes(dmg, e, player, log):
            player.modify_stat("brutality", r["brutality_gain"])
            player.wrath = 0
            log.append(S["runic_hit"].format(name=e["name_short"]))
        else:
            log.append(S["runic_miss"])

    elif action_id == "mercy":
        m = A["mercy"]
        e["current_hp"] = 0
        player.modify_stat("mercy", m["mercy_gain"])
        player.modify_stat("honour", m["honour_gain"])
        log.append(S["mercy"])

    elif action_id == "flee":
        dmg = roll_range(*A["flee"]["dmg"])
        player.take_damage(dmg)
        player.modify_stat("honour", A["flee"]["honour_loss"])
        log.append(S["flee_1"])
        log.append(S["flee_2"])
        log.append(S["flee_cost"].format(damage=damage_word(dmg)))
        combat_state["fled"] = True
        combat_state["over"] = True
        return combat_state

    # ── Check enemy death ─────────────────────────────────────
    if e["current_hp"] <= 0:
        _resolve_enemy_death(e, player, combat_state, log)
        combat_state["over"] = True
        combat_state["won"] = True
        return combat_state

    # ── Phase transitions (boss) ──────────────────────────────
    if e.get("phases"):
        ratio = e["current_hp"] / e["hp"]
        if e["current_phase"] == 1 and ratio <= CC["phase2_hp_ratio"]:
            e["current_phase"] = 2
            log.append(e["phrases"].get("phase2", ""))
        elif e["current_phase"] == 2 and ratio <= CC["phase3_hp_ratio"]:
            e["current_phase"] = 3
            log.append(e["phrases"].get("phase3", ""))

    # ── Effects tick ──────────────────────────────────────────
    if not combat_state["over"]:
        _tick_effects(e, log)
        if e["current_hp"] <= 0:
            _resolve_enemy_death(e, player, combat_state, log)
            combat_state["over"] = True
            combat_state["won"] = True
            return combat_state

    # ── Enemy turn ────────────────────────────────────────────
    if not combat_state["over"]:
        _resolve_enemy_turn(e, player, log, combat_state)

    # Taunt
    if "taunt" in e.get("phrases", {}) and chance(CC["taunt_chance"]):
        log.append(random.choice(e["phrases"]["taunt"]))

    # Check player death
    if player.is_dead():
        _handle_player_death(player, combat_state, log)

    return combat_state


def _handle_player_death(player, combat_state, log) -> dict:
    log.append(S["player_death_1"])
    log.append(S["player_death_2"])
    player.deaths += 1
    player.modify_stat("curse_stacks", 1)
    player.echo_shards = player.echo_shards // CC["death_shard_divisor"]
    player.health = player.max_health
    combat_state["over"] = True
    combat_state["died"] = True
    return combat_state


def _tick_player_effects(combat_state, player, log):
    effects = combat_state.get("player_effects", {})
    if "bleeding" in effects:
        dmg = roll_range(*CC["bleeding"]["dmg"])
        player.take_damage(dmg)
        log.append(S["bleeding_tick_player"].format(dmg=dmg))
        effects["bleeding"] -= 1
        if effects["bleeding"] <= 0:
            del effects["bleeding"]
            log.append(S["bleeding_slow"])


def _resolve_enemy_turn(e, player, log, combat_state=None):
    windup = random.choice(e["phrases"]["windup"])
    log.append(windup)
    dmg_range = e["damage"]
    if e.get("shield") and not e.get("flanked"):
        bonus = CC["shield_enemy_dmg_bonus"]
        dmg_range = (dmg_range[0] + bonus[0], dmg_range[1] + bonus[1])
    if chance(e["accuracy"]):
        dmg = roll_range(*dmg_range)
        shield_def = EQUIPMENT.get(player.equipped.get("shield", ""), {}).get(
            "defense", 0
        )
        dmg = max(1, dmg - shield_def)
        actual = player.take_damage(dmg)
        player.modify_stat("wrath", CC["wrath_hit_by_enemy"])
        log.append(random.choice(e["phrases"]["hit"]))
        log.append(f"— {damage_word(actual)} taken.")
        # on_hit_drain — enemy drains a player stat on successful hit
        drain_cfg = e.get("on_hit_drain")
        if drain_cfg:
            stat = drain_cfg["stat"]
            amount = drain_cfg["amount"]
            current = getattr(player, stat, 0)
            drained = min(amount, current)
            if drained > 0:
                setattr(player, stat, current - drained)
                log.append(
                    random.choice(
                        e["phrases"].get(
                            "drain_trigger",
                            [f"Something is drawn out of you — {drained} lost."],
                        )
                    )
                )
        # Enemy weapon effect
        effect = e.get("weapon", {}).get("effect")
        if effect == "bleeding" and combat_state is not None:
            peff = combat_state.setdefault("player_effects", {})
            if not peff.get("bleeding"):
                peff["bleeding"] = CC["bleeding"]["duration"]
                log.append(S["bleeding_open_player"])
    else:
        log.append(random.choice(e["phrases"]["miss"]))


def _resolve_enemy_death(e, player, combat_state, log):
    log.append(random.choice(e["phrases"]["death"]))
    lo, hi = e["shards"]
    shards = roll_range(lo, hi)
    player.echo_shards += shards
    combat_state["shards_gained"] = shards
    for item, prob in e.get("loot", []):
        if chance(prob):
            player.add_item(item)
            combat_state["items_gained"].append(item)
    on_death = e.get("on_death", {})
    if "flag" in on_death:
        player.set_flag(on_death["flag"], True)
    if "memory" in on_death:
        key, label = on_death["memory"]
        player.add_memory(key, label)
    player.set_flag(f"defeated_{e['key']}", True)


def _tick_effects(e, log):
    effects = e.get("effects", {})
    if "bleeding" in effects:
        dmg = roll_range(*CC["bleeding"]["dmg"])
        e["current_hp"] = max(0, e["current_hp"] - dmg)
        log.append(S["bleeding_tick_enemy"].format(name=e["name_short"], dmg=dmg))
        effects["bleeding"] -= 1
        if effects["bleeding"] <= 0:
            del effects["bleeding"]
            log.append(S["bleeding_slow"])


def _player_strikes(dmg, e, player, log) -> bool:
    """Apply player strike with evasion check. Returns True if hit landed."""
    if e.get("evasion", 0) > 0 and chance(e["evasion"]):
        log.append(
            random.choice(
                e["phrases"].get(
                    "evade", ["It moves before you do. The blow finds nothing."]
                )
            )
        )
        return False
    _hit_enemy(dmg, e, player, log)
    return True


def _hit_enemy(dmg, e, player, log):
    e["current_hp"] = max(0, e["current_hp"] - dmg)
    # Weapon effect — apply on hit if weapon carries one
    if e["current_hp"] > 0:
        weapon = player.equipped.get("weapon", "bare hands")
        effect = EQUIPMENT.get(weapon, {}).get("effect")
        if effect == "bleeding" and not e.get("effects", {}).get("bleeding"):
            e.setdefault("effects", {})["bleeding"] = CC["bleeding"]["duration"]
            log.append(S["bleeding_open_enemy"])
    # Drain mechanic — enemy heals from player stat when hit
    if e.get("drain"):
        drain = min(e["drain_amount"], getattr(player, "wrath", 0))
        if drain > 0:
            player.wrath = max(0, player.wrath - drain)
            heal = min(drain, e["hp"] - e["current_hp"])
            e["current_hp"] = min(e["hp"], e["current_hp"] + heal)
            log.append(random.choice(e["phrases"]["drain_trigger"]))


def _apply_mods(base, player, kind):
    mod = base
    for slot in ("weapon", "body"):
        item = player.equipped.get(slot, "") or (
            "bare hands" if slot == "weapon" else ""
        )
        mod += EQUIPMENT.get(item, {}).get("damage_bonus", 0)
    for m in COMBAT_MODS:
        if "fn" in m:
            applies = getattr(player, m["fn"])()
        else:
            applies = getattr(player, m["stat"], 0) > m["gt"]
        if "action" in m and m["action"] != kind:
            applies = False
        if applies:
            if "bonus_die" in m:
                mod += roll(m["bonus_die"])
            if "penalty_die" in m:
                mod -= roll(m["penalty_die"])
    return max(1, mod)
