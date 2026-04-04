"""Tests for engine/state.py — PlayerState logic."""

from engine.state import PlayerState

# ── modify_stat ───────────────────────────────────────────────


def test_modify_stat_basic():
    s = PlayerState()
    s.modify_stat("honour", 10)
    assert s.honour == 60


def test_modify_stat_clamps_at_max():
    s = PlayerState()
    s.modify_stat("honour", 9999)
    assert s.honour == 100


def test_modify_stat_clamps_at_min():
    s = PlayerState()
    s.modify_stat("honour", -9999)
    assert s.honour == 0


def test_modify_stat_echo_shards_no_upper_cap():
    s = PlayerState()
    s.modify_stat("echo_shards", 99999)
    assert s.echo_shards == 99999


def test_modify_stat_echo_shards_no_negative():
    s = PlayerState()
    s.modify_stat("echo_shards", -1)
    assert s.echo_shards == 0


def test_modify_stat_unknown_stat_is_noop():
    s = PlayerState()
    s.modify_stat("nonexistent_stat", 50)  # should not raise


# ── heal / take_damage ────────────────────────────────────────


def test_take_damage_reduces_health():
    s = PlayerState()
    s.take_damage(30)
    assert s.health == 70


def test_take_damage_does_not_go_below_zero():
    s = PlayerState()
    s.take_damage(9999)
    assert s.health == 0


def test_heal_restores_health():
    s = PlayerState()
    s.health = 50
    s.heal(20)
    assert s.health == 70


def test_heal_does_not_exceed_max():
    s = PlayerState()
    s.health = 90
    s.heal(9999)
    assert s.health == s.max_health


def test_is_dead_true_at_zero():
    s = PlayerState()
    s.health = 0
    assert s.is_dead()


def test_is_dead_false_above_zero():
    s = PlayerState()
    assert not s.is_dead()


# ── add_item ──────────────────────────────────────────────────


def test_add_item_adds_to_inventory():
    s = PlayerState()
    s.add_item("iron scraps")
    assert "iron scraps" in s.inventory


def test_add_item_no_duplicates():
    s = PlayerState()
    s.add_item("iron scraps")
    s.add_item("iron scraps")
    assert s.inventory.count("iron scraps") == 1


def test_add_item_auto_equips_weapon():
    s = PlayerState()
    s.add_item("sharpened axe")
    assert s.equipped["weapon"] == "sharpened axe"


def test_add_item_higher_tier_replaces_lower():
    s = PlayerState()
    s.add_item("sharpened axe")  # tier 2
    s.add_item("Gunnar's Axe")  # tier 3
    assert s.equipped["weapon"] == "Gunnar's Axe"


def test_add_item_lower_tier_does_not_replace():
    s = PlayerState()
    s.add_item("Gunnar's Axe")  # tier 3
    s.add_item("sharpened axe")  # tier 2
    assert s.equipped["weapon"] == "Gunnar's Axe"


def test_add_item_body_slot():
    s = PlayerState()
    s.add_item("wolf pelt")
    assert s.equipped["body"] == "wolf pelt"


def test_add_item_bear_pelt_replaces_wolf_pelt():
    s = PlayerState()
    s.add_item("wolf pelt")  # tier 1
    s.add_item("bear pelt")  # tier 2
    assert s.equipped["body"] == "bear pelt"


# ── remove_item ───────────────────────────────────────────────


def test_remove_item_removes_from_inventory():
    s = PlayerState()
    s.add_item("iron scraps")
    s.remove_item("iron scraps")
    assert "iron scraps" not in s.inventory


def test_remove_item_returns_true_on_success():
    s = PlayerState()
    s.add_item("iron scraps")
    assert s.remove_item("iron scraps") is True


def test_remove_item_returns_false_if_not_present():
    s = PlayerState()
    assert s.remove_item("nonexistent item") is False


def test_remove_item_unequips_weapon():
    s = PlayerState()
    s.add_item("sharpened axe")
    s.remove_item("sharpened axe")
    assert s.equipped["weapon"] == ""


def test_remove_item_falls_back_to_best_remaining():
    """Removing bear pelt should auto-equip wolf pelt."""
    s = PlayerState()
    s.add_item("wolf pelt")  # tier 1
    s.add_item("bear pelt")  # tier 2 — now equipped
    assert s.equipped["body"] == "bear pelt"
    s.remove_item("bear pelt")
    assert s.equipped["body"] == "wolf pelt"


def test_remove_item_no_fallback_when_slot_empty():
    s = PlayerState()
    s.add_item("wolf pelt")
    s.remove_item("wolf pelt")
    assert s.equipped["body"] == ""


# ── flags / memories ─────────────────────────────────────────


def test_set_and_check_flag():
    s = PlayerState()
    s.set_flag("wolf_killed")
    assert s.has_flag("wolf_killed")


def test_missing_flag_is_false():
    s = PlayerState()
    assert not s.has_flag("wolf_killed")


def test_add_memory_once():
    s = PlayerState()
    assert s.add_memory("the_death", "The Death") is True
    assert s.has_memory("the_death")


def test_add_memory_duplicate_returns_false():
    s = PlayerState()
    s.add_memory("the_death", "The Death")
    assert s.add_memory("the_death", "The Death") is False
    assert s.memories.count("the_death") == 1


# ── serialisation ─────────────────────────────────────────────


def test_round_trip_serialisation():
    s = PlayerState()
    s.name = "Geirr"
    s.honour = 75
    s.add_item("wolf pelt")
    s.set_flag("wolf_killed")
    s.add_memory("the_death", "The Death")

    restored = PlayerState.from_dict(s.to_dict())
    assert restored.name == "Geirr"
    assert restored.honour == 75
    assert "wolf pelt" in restored.inventory
    assert restored.has_flag("wolf_killed")
    assert restored.has_memory("the_death")
