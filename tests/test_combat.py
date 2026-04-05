"""Tests for engine/combat.py — action resolution."""

import pytest
from unittest.mock import patch
from engine.state import PlayerState
from engine.combat import start_combat, get_player_actions, resolve_action
from content.game_config import COMBAT_CONFIG


@pytest.fixture
def player():
    s = PlayerState()
    s.health = 100
    s.echo_shards = 0
    s.honour = 50
    return s


@pytest.fixture
def rat_combat(player):
    return start_combat("rat", player)


@pytest.fixture
def wolf_combat(player):
    return start_combat("wolf", player)


# ── start_combat ──────────────────────────────────────────────


def test_start_combat_initialises_enemy(player):
    cs = start_combat("rat", player)
    e = cs["enemy"]
    assert e["current_hp"] == e["hp"]
    assert cs["over"] is False
    assert cs["won"] is False
    assert cs["fled"] is False


def test_start_combat_curse_scales_damage(player):
    player.curse_stacks = 5
    cs = start_combat("rat", player)
    base_min = 3  # rat base damage min
    assert cs["enemy"]["damage"][0] > base_min


def test_start_combat_variant_overrides(player):
    cs_normal = start_combat("wolf", player)
    cs_dire = start_combat("dire_wolf", player)
    assert cs_dire["enemy"]["hp"] > cs_normal["enemy"]["hp"]


# ── get_player_actions ────────────────────────────────────────


def test_actions_always_include_light_heavy(player, rat_combat):
    actions = get_player_actions(rat_combat, player)
    ids = [a["id"] for a in actions]
    assert "light" in ids
    assert "heavy" in ids


def test_actions_include_flee_without_berserk(player, rat_combat):
    actions = get_player_actions(rat_combat, player)
    ids = [a["id"] for a in actions]
    assert "flee" in ids


def test_actions_no_flee_with_berserk(player):
    player.add_item("bear pelt")  # tier 2 body with berserk
    cs = start_combat("rat", player)
    actions = get_player_actions(cs, player)
    ids = [a["id"] for a in actions]
    assert "flee" not in ids
    assert "parry" not in ids
    assert "mercy" not in ids


def test_actions_runic_requires_shards(player, rat_combat):
    player.echo_shards = 0
    actions = get_player_actions(rat_combat, player)
    assert "runic" not in [a["id"] for a in actions]

    player.echo_shards = 100
    actions = get_player_actions(rat_combat, player)
    assert "runic" in [a["id"] for a in actions]


def test_actions_mercy_requires_low_enemy_hp(player, rat_combat):
    player.honour = 80
    rat_combat["enemy"]["current_hp"] = rat_combat["enemy"]["hp"]  # full hp
    actions = get_player_actions(rat_combat, player)
    assert "mercy" not in [a["id"] for a in actions]


# ── resolve_action: flee ──────────────────────────────────────


def test_flee_ends_combat(player, rat_combat):
    with patch("engine.combat.roll_range", return_value=5):
        cs = resolve_action("flee", rat_combat, player)
    assert cs["fled"] is True
    assert cs["over"] is True
    assert cs["won"] is False


def test_flee_costs_health(player, rat_combat):
    with patch("engine.combat.roll_range", return_value=10):
        resolve_action("flee", rat_combat, player)
    assert player.health < 100


# ── resolve_action: mercy ─────────────────────────────────────


def test_mercy_ends_combat_as_won(player, rat_combat):
    rat_combat["enemy"]["current_hp"] = 1
    with patch("engine.combat.chance", return_value=False):
        cs = resolve_action("mercy", rat_combat, player)
    assert cs["won"] is True
    assert cs["over"] is True


def test_mercy_raises_mercy_stat(player, rat_combat):
    rat_combat["enemy"]["current_hp"] = 1
    mercy_before = player.mercy
    with patch("engine.combat.chance", return_value=False):
        resolve_action("mercy", rat_combat, player)
    assert player.mercy > mercy_before


# ── resolve_action: light strike ─────────────────────────────


def test_light_strike_hits_enemy(player, rat_combat):
    with patch("engine.combat.roll_range", return_value=15), patch(
        "engine.combat.chance", return_value=False
    ):
        cs = resolve_action("light", rat_combat, player)
    assert cs["enemy"]["current_hp"] < cs["enemy"]["hp"]


def test_light_strike_killing_blow_ends_combat(player, rat_combat):
    rat_combat["enemy"]["current_hp"] = 1
    with patch("engine.combat.roll_range", return_value=50), patch(
        "engine.combat.chance", return_value=False
    ):
        cs = resolve_action("light", rat_combat, player)
    assert cs["won"] is True
    assert cs["over"] is True


# ── resolve_action: runic burst ───────────────────────────────


def test_runic_costs_shards(player, rat_combat):
    player.echo_shards = 100
    rat_combat["enemy"]["current_hp"] = 9999  # ensure rat survives — no shard reward
    with patch("engine.combat.roll_range", return_value=5), patch(
        "engine.combat.chance", return_value=False
    ):
        resolve_action("runic", rat_combat, player)
    assert player.echo_shards == 0


def test_runic_resets_wrath(player, rat_combat):
    player.wrath = 60
    player.echo_shards = 100
    with patch("engine.combat.roll_range", return_value=30), patch(
        "engine.combat.chance", return_value=False
    ):
        resolve_action("runic", rat_combat, player)
    assert player.wrath == 0


# ── player death ──────────────────────────────────────────────


# ── resolve_action: heavy strike — brutality ─────────────────


def test_heavy_strike_gains_brutality(player, rat_combat):
    rat_combat["enemy"]["current_hp"] = 9999
    brutality_before = player.brutality
    # chance calls: overcommit→False, accuracy→False (enemy misses)
    with patch("engine.combat.roll_range", return_value=20), patch(
        "engine.combat.chance", return_value=False
    ):
        resolve_action("heavy", rat_combat, player)
    assert (
        player.brutality
        == brutality_before + COMBAT_CONFIG["actions"]["heavy"]["brutality_gain"]
    )


def test_heavy_killing_blow_extra_brutality(player, rat_combat):
    rat_combat["enemy"]["current_hp"] = 1
    brutality_before = player.brutality
    # chance calls: overcommit→False, rat loot×2→False
    with patch("engine.combat.roll_range", return_value=20), patch(
        "engine.combat.chance", side_effect=[False, False, False]
    ):
        cs = resolve_action("heavy", rat_combat, player)
    assert cs["won"] is True
    expected = (
        brutality_before
        + COMBAT_CONFIG["actions"]["heavy"]["brutality_gain"]
        + COMBAT_CONFIG["actions"]["heavy"]["kill_brutality_bonus"]
    )
    assert player.brutality == expected


def test_heavy_miss_no_brutality(player, rat_combat):
    rat_combat["enemy"]["current_hp"] = 9999
    brutality_before = player.brutality
    # chance: overcommit→True (overcommit fires, strike is skipped)
    with patch("engine.combat.roll_range", return_value=1), patch(
        "engine.combat.chance", side_effect=[True, False]
    ):
        resolve_action("heavy", rat_combat, player)
    assert player.brutality == brutality_before


# ── resolve_action: near-death resolve loss ───────────────────


def test_near_death_loses_resolve(player, rat_combat):
    player.health = 15  # already below 20% threshold
    rat_combat["enemy"]["current_hp"] = 9999
    resolve_before = player.resolve
    # chance: accuracy→True (enemy hits, triggering near-death check)
    with patch("engine.combat.roll_range", return_value=1), patch(
        "engine.combat.chance", return_value=True
    ):
        resolve_action("light", rat_combat, player)
    assert player.resolve < resolve_before
    assert rat_combat["near_death_triggered"] is True


def test_near_death_triggers_once(player, rat_combat):
    player.health = 15
    rat_combat["enemy"]["current_hp"] = 9999
    rat_combat["near_death_triggered"] = True  # already fired this combat
    resolve_before = player.resolve
    with patch("engine.combat.roll_range", return_value=1), patch(
        "engine.combat.chance", return_value=True
    ):
        resolve_action("light", rat_combat, player)
    assert player.resolve == resolve_before


# ── resolve_action: phase transition resolve loss ─────────────


def test_phase_transition_loses_resolve(player):
    cs = start_combat("gunnar", player)
    # Phase 2 triggers at HP <= 0.65 * 120 = 78; set to 79
    cs["enemy"]["current_hp"] = 79
    resolve_before = player.resolve
    # chance: accuracy→False (enemy misses), taunt→False
    with patch("engine.combat.roll_range", return_value=2), patch(
        "engine.combat.chance", return_value=False
    ):
        resolve_action("light", cs, player)
    assert cs["enemy"]["current_phase"] == 2
    assert player.resolve == resolve_before + COMBAT_CONFIG["phase_resolve_loss"]


# ── player death ──────────────────────────────────────────────


def test_player_death_ends_combat(player, rat_combat):
    player.health = 1
    # Force a hit via enemy turn — patch accuracy to always hit
    with patch("engine.combat.roll_range", return_value=5), patch(
        "engine.combat.chance", return_value=False
    ), patch("engine.combat.roll", return_value=1):
        # Tick player effects (none), then light strike, then enemy hits
        rat_combat["player_effects"][
            "bleeding"
        ] = 1  # duration counter (int), not a dict
        cs = resolve_action("light", rat_combat, player)
    assert cs["over"] is True
    assert cs.get("died") is True
