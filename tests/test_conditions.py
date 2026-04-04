"""Tests for engine/conditions.py — eval_condition DSL."""
import pytest
from engine.conditions import eval_condition
from engine.state import PlayerState


@pytest.fixture
def state():
    s = PlayerState()
    s.set_flag("wolf_killed")
    s.add_memory("the_death", "The Death")
    s.add_item("iron scraps")
    s.add_item("sharpened axe")   # auto-equips as weapon
    s.honour = 70
    s.brutality = 20
    return s


# ── None ──────────────────────────────────────────────────────

def test_none_condition_is_always_true(state):
    assert eval_condition(None, state) is True


# ── flag ──────────────────────────────────────────────────────

def test_flag_true_when_set(state):
    assert eval_condition({"flag": "wolf_killed"}, state) is True


def test_flag_false_when_not_set(state):
    assert eval_condition({"flag": "wolf_spared"}, state) is False


# ── memory ────────────────────────────────────────────────────

def test_memory_true_when_present(state):
    assert eval_condition({"memory": "the_death"}, state) is True


def test_memory_false_when_absent(state):
    assert eval_condition({"memory": "the_feast"}, state) is False


# ── has_item ──────────────────────────────────────────────────

def test_has_item_true(state):
    assert eval_condition({"has_item": "iron scraps"}, state) is True


def test_has_item_false(state):
    assert eval_condition({"has_item": "bear pelt"}, state) is False


# ── equipped ──────────────────────────────────────────────────

def test_equipped_true(state):
    assert eval_condition({"equipped": "sharpened axe"}, state) is True


def test_equipped_false(state):
    assert eval_condition({"equipped": "rusted axe"}, state) is False


# ── stat_gte ──────────────────────────────────────────────────

def test_stat_gte_true(state):
    assert eval_condition({"stat_gte": "honour", "value": 70}, state) is True


def test_stat_gte_false(state):
    assert eval_condition({"stat_gte": "honour", "value": 71}, state) is False


def test_stat_gte_unknown_stat_returns_false(state):
    # getattr default 0 — unknown stat is treated as 0
    assert eval_condition({"stat_gte": "nonexistent", "value": 1}, state) is False


def test_stat_gte_unknown_stat_zero_threshold(state):
    assert eval_condition({"stat_gte": "nonexistent", "value": 0}, state) is True


# ── not ───────────────────────────────────────────────────────

def test_not_inverts_true(state):
    assert eval_condition({"not": {"flag": "wolf_killed"}}, state) is False


def test_not_inverts_false(state):
    assert eval_condition({"not": {"flag": "wolf_spared"}}, state) is True


# ── and ───────────────────────────────────────────────────────

def test_and_all_true(state):
    cond = {"and": [{"flag": "wolf_killed"}, {"has_item": "iron scraps"}]}
    assert eval_condition(cond, state) is True


def test_and_one_false(state):
    cond = {"and": [{"flag": "wolf_killed"}, {"flag": "wolf_spared"}]}
    assert eval_condition(cond, state) is False


def test_and_empty_is_true(state):
    assert eval_condition({"and": []}, state) is True


# ── or ────────────────────────────────────────────────────────

def test_or_one_true(state):
    cond = {"or": [{"flag": "wolf_spared"}, {"flag": "wolf_killed"}]}
    assert eval_condition(cond, state) is True


def test_or_all_false(state):
    cond = {"or": [{"flag": "wolf_spared"}, {"flag": "bear_killed"}]}
    assert eval_condition(cond, state) is False


def test_or_empty_is_false(state):
    assert eval_condition({"or": []}, state) is False


# ── nested ────────────────────────────────────────────────────

def test_nested_and_or(state):
    # (wolf_killed AND honour>=70) OR has_item bear_pelt
    cond = {
        "or": [
            {"and": [{"flag": "wolf_killed"}, {"stat_gte": "honour", "value": 70}]},
            {"has_item": "bear pelt"},
        ]
    }
    assert eval_condition(cond, state) is True


def test_nested_not_and(state):
    cond = {"not": {"and": [{"flag": "wolf_killed"}, {"flag": "wolf_spared"}]}}
    assert eval_condition(cond, state) is True


# ── unknown key raises ────────────────────────────────────────

def test_unknown_condition_key_raises(state):
    with pytest.raises(ValueError):
        eval_condition({"unknown_key": "value"}, state)
