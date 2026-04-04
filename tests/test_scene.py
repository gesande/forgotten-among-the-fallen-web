"""Tests for engine/scene.py — render_scene, apply_choice, beat processing."""

import pytest
from unittest.mock import patch
from engine.state import PlayerState
from engine.scene import render_scene, apply_choice, has_prose_beats, _build_hud

# ── Minimal fake SCENES used across tests ─────────────────────

FAKE_SCENES = {
    "prose_scene": {
        "art": "test_art",
        "beats": [
            {"type": "prose", "text": "The mist is cold."},
            {"type": "italic", "text": "You remember nothing."},
        ],
        "choices": [
            {"label": "Press on", "next": "next_scene"},
        ],
    },
    "stat_scene": {
        "art": "test_art",
        "beats": [
            {"type": "stat", "changes": {"honour": 10, "echo_shards": 50}},
        ],
        "next": "next_scene",
    },
    "flag_scene": {
        "art": "test_art",
        "beats": [
            {"type": "flag", "key": "test_flag"},
        ],
        "next": "next_scene",
    },
    "item_give_scene": {
        "art": "test_art",
        "beats": [
            {"type": "item", "action": "give", "item": "iron scraps"},
        ],
        "next": "next_scene",
    },
    "item_take_scene": {
        "art": "test_art",
        "beats": [
            {"type": "item", "action": "take", "item": "iron scraps"},
        ],
        "next": "next_scene",
    },
    "heal_scene": {
        "art": "test_art",
        "beats": [
            {"type": "heal", "amount": 30},
        ],
        "next": "next_scene",
    },
    "memory_scene": {
        "art": "test_art",
        "beats": [
            {
                "type": "memory",
                "key": "the_oath",
                "label": "The Oath",
                "text": "You swore once.",
            },
        ],
        "next": "next_scene",
    },
    "conditional_prose_scene": {
        "art": "test_art",
        "beats": [
            {
                "type": "conditional_prose",
                "variants": [
                    {
                        "condition": {"flag": "wolf_killed"},
                        "text": "You remember the wolf.",
                    },
                    {"text": "You remember nothing."},
                ],
            }
        ],
        "next": "next_scene",
    },
    "combat_scene": {
        "art": "test_art",
        "beats": [
            {"type": "combat", "enemy": "rat"},
        ],
        "next": "next_scene",
    },
    "beat_condition_scene": {
        "art": "test_art",
        "beats": [
            {"type": "prose", "text": "Hidden.", "condition": {"flag": "secret"}},
            {"type": "prose", "text": "Always shown."},
        ],
        "next": "next_scene",
    },
    "choice_condition_scene": {
        "art": "test_art",
        "beats": [],
        "choices": [
            {
                "label": "For the honoured",
                "next": "a",
                "condition": {"stat_gte": "honour", "value": 80},
            },
            {"label": "Always available", "next": "b"},
        ],
    },
    "auto_advance_scene": {
        "art": "test_art",
        "beats": [],
        "next": "next_scene",
    },
    "continue_button_scene": {
        "art": "test_art",
        "beats": [
            {"type": "prose", "text": "Read this."},
        ],
        "next": "next_scene",
    },
    "apply_choice_scene": {
        "art": "test_art",
        "beats": [],
        "choices": [
            {
                "label": "The merciful path",
                "next": "mercy_scene",
                "effects": {"mercy": 5},
                "flags": {"chose_mercy": True},
            },
            {
                "label": "Take the scraps",
                "next": "loot_scene",
                "item": "iron scraps",
            },
        ],
    },
    "choice_remove_item_scene": {
        "art": "test_art",
        "beats": [],
        "choices": [
            {
                "label": "Give it up.",
                "next": "next_scene",
                "remove_item": "iron scraps",
            },
        ],
    },
    "choice_heal_scene": {
        "art": "test_art",
        "beats": [],
        "choices": [
            {"label": "Rest", "next": "next_scene", "heal": 20},
        ],
    },
    # ── Offering scenes (item removal via beat) ───────────────
    "offering_scene": {
        "art": "test_art",
        "beats": [],
        "choices": [
            {
                "label": "Leave the axe.",
                "next": "offered_axe_scene",
                "condition": {"has_item": "Gunnar's Axe"},
                "flags": {"offered_axe": True},
                "effects": {"honour": 10},
            },
            {
                "label": "Leave the pelt.",
                "next": "offered_pelt_scene",
                "condition": {"has_item": "bear pelt"},
                "flags": {"offered_pelt": True},
                "effects": {"honour": 5, "brutality": -5},
            },
            {
                "label": "Enter anyway.",
                "next": "interior_scene",
            },
        ],
    },
    "offered_axe_scene": {
        "art": "test_art",
        "beats": [
            {"type": "item", "action": "take", "item": "Gunnar's Axe"},
            {"type": "prose", "text": "It was never yours."},
        ],
        "choices": [{"label": "Enter.", "next": "interior_scene"}],
    },
    "offered_pelt_scene": {
        "art": "test_art",
        "beats": [
            {"type": "item", "action": "take", "item": "bear pelt"},
            {"type": "prose", "text": "You do not know what you are leaving behind."},
        ],
        "choices": [{"label": "Enter.", "next": "interior_scene"}],
    },
    "interior_scene": {
        "art": "test_art",
        "beats": [
            {
                "type": "conditional_prose",
                "variants": [
                    {
                        "condition": {"flag": "offered_axe"},
                        "text": "He sees your empty hand.",
                    },
                    {
                        "condition": {"flag": "offered_pelt"},
                        "text": "He glances toward the door.",
                    },
                ],
            },
            {"type": "prose", "text": "He is sitting on the floor."},
        ],
        "next": "next_scene",
    },
}


@pytest.fixture(autouse=True)
def patch_scenes():
    with patch("engine.scene.SCENES", FAKE_SCENES):
        yield


@pytest.fixture
def player():
    return PlayerState()


# ── render_scene: error handling ──────────────────────────────


def test_unknown_scene_returns_error(player):
    result = render_scene("nonexistent_scene", player)
    assert "error" in result


# ── render_scene: first-visit flag ────────────────────────────


def test_first_visit_sets_visited_flag(player):
    render_scene("prose_scene", player)
    assert player.has_flag("scene_visited_prose_scene")


def test_second_visit_does_not_reapply_stat(player):
    render_scene("stat_scene", player)
    honour_after_first = player.honour
    render_scene("stat_scene", player)
    assert player.honour == honour_after_first


# ── render_scene: beat types ──────────────────────────────────


def test_prose_beat_renders_paragraph(player):
    out = render_scene("prose_scene", player)
    types = [p["type"] for p in out["paragraphs"]]
    assert "prose" in types


def test_italic_beat_renders_italic(player):
    out = render_scene("prose_scene", player)
    types = [p["type"] for p in out["paragraphs"]]
    assert "italic" in types


def test_stat_beat_modifies_player_on_first_visit(player):
    render_scene("stat_scene", player)
    assert player.honour == 60  # default 50 + 10


def test_stat_beat_tracks_shards_in_output(player):
    out = render_scene("stat_scene", player)
    assert out["shards"] == 50


def test_flag_beat_sets_flag_on_first_visit(player):
    render_scene("flag_scene", player)
    assert player.has_flag("test_flag")


def test_flag_beat_not_reapplied_on_revisit(player):
    render_scene("flag_scene", player)
    player.set_flag("test_flag", False)  # manually clear
    render_scene("flag_scene", player)  # second visit — should not re-set
    assert not player.has_flag("test_flag")


def test_item_give_beat_adds_item(player):
    render_scene("item_give_scene", player)
    assert "iron scraps" in player.inventory


def test_item_give_only_on_first_visit(player):
    render_scene("item_give_scene", player)
    render_scene("item_give_scene", player)
    assert player.inventory.count("iron scraps") == 1


def test_item_take_beat_removes_item(player):
    player.add_item("iron scraps")
    render_scene("item_take_scene", player)
    assert "iron scraps" not in player.inventory


def test_heal_beat_restores_hp(player):
    player.health = 50
    render_scene("heal_scene", player)
    assert player.health == 80


def test_heal_beat_only_on_first_visit(player):
    player.health = 50
    render_scene("heal_scene", player)
    player.health = 50  # manually reduce again
    render_scene("heal_scene", player)  # second visit — no heal
    assert player.health == 50


# ── render_scene: memory beat ─────────────────────────────────


def test_memory_beat_adds_memory(player):
    render_scene("memory_scene", player)
    assert player.has_memory("the_oath")


def test_memory_beat_adds_paragraph(player):
    out = render_scene("memory_scene", player)
    types = [p["type"] for p in out["paragraphs"]]
    assert "memory" in types


def test_memory_beat_idempotent(player):
    render_scene("memory_scene", player)
    out2 = render_scene("memory_scene", player)
    memory_paragraphs = [p for p in out2["paragraphs"] if p["type"] == "memory"]
    assert len(memory_paragraphs) == 0  # already had memory — not added again


# ── render_scene: conditional_prose ──────────────────────────


def test_conditional_prose_first_matching_variant(player):
    player.set_flag("wolf_killed")
    out = render_scene("conditional_prose_scene", player)
    assert out["paragraphs"][0]["text"] == "You remember the wolf."


def test_conditional_prose_fallback_variant(player):
    out = render_scene("conditional_prose_scene", player)
    assert out["paragraphs"][0]["text"] == "You remember nothing."


# ── render_scene: beat condition gate ────────────────────────


def test_beat_condition_hides_prose_when_false(player):
    out = render_scene("beat_condition_scene", player)
    texts = [p["text"] for p in out["paragraphs"]]
    assert "Hidden." not in texts
    assert "Always shown." in texts


def test_beat_condition_shows_prose_when_true(player):
    player.set_flag("secret")
    out = render_scene("beat_condition_scene", player)
    texts = [p["text"] for p in out["paragraphs"]]
    assert "Hidden." in texts


# ── render_scene: combat beat ─────────────────────────────────


def test_combat_beat_triggers_combat(player):
    out = render_scene("combat_scene", player)
    assert out["combat"] is not None
    assert out["combat"]["enemy_key"] == "rat"


def test_combat_beat_skipped_when_already_defeated(player):
    player.set_flag("defeated_rat")
    out = render_scene("combat_scene", player)
    assert out["combat"] is None


# ── render_scene: choices ─────────────────────────────────────


def test_choices_filtered_by_condition_false(player):
    player.honour = 50  # below 80
    out = render_scene("choice_condition_scene", player)
    labels = [c["label"] for c in out["choices"]]
    assert "For the honoured" not in labels
    assert "Always available" in labels


def test_choices_pass_condition_when_met(player):
    player.honour = 80
    out = render_scene("choice_condition_scene", player)
    labels = [c["label"] for c in out["choices"]]
    assert "For the honoured" in labels


# ── render_scene: auto-advance / continue button ──────────────


def test_auto_advance_when_no_prose(player):
    out = render_scene("auto_advance_scene", player)
    assert out["next"] == "next_scene"
    assert out["choices"] == []


def test_continue_button_when_has_prose(player):
    out = render_scene("continue_button_scene", player)
    assert out["next"] is None
    assert any(c["id"] == "__next__" for c in out["choices"])


# ── apply_choice ──────────────────────────────────────────────


def test_apply_choice_returns_next_scene(player):
    next_key, _ = apply_choice("apply_choice_scene", "0", player)
    assert next_key == "mercy_scene"


def test_apply_choice_applies_stat_effect(player):
    apply_choice("apply_choice_scene", "0", player)
    assert player.mercy == 5


def test_apply_choice_sets_flag(player):
    apply_choice("apply_choice_scene", "0", player)
    assert player.has_flag("chose_mercy")


def test_apply_choice_gives_item(player):
    apply_choice("apply_choice_scene", "1", player)
    assert "iron scraps" in player.inventory


def test_apply_choice_heal(player):
    player.health = 60
    apply_choice("choice_heal_scene", "0", player)
    assert player.health == 80


def test_apply_choice_remove_item(player):
    player.add_item("iron scraps")
    apply_choice("choice_remove_item_scene", "0", player)
    assert "iron scraps" not in player.inventory


def test_apply_choice_filters_by_condition(player):
    # Scene has conditional choice — only available choice when condition fails
    # is "Always available" (id 0 after filtering)
    player.honour = 50
    out = render_scene("choice_condition_scene", player)
    assert len(out["choices"]) == 1
    assert out["choices"][0]["label"] == "Always available"


# ── offering mechanic ─────────────────────────────────────────


def test_offering_axe_choice_hidden_without_item(player):
    out = render_scene("offering_scene", player)
    labels = [c["label"] for c in out["choices"]]
    assert "Leave the axe." not in labels


def test_offering_axe_choice_visible_with_item(player):
    player.add_item("Gunnar's Axe")
    out = render_scene("offering_scene", player)
    labels = [c["label"] for c in out["choices"]]
    assert "Leave the axe." in labels


def test_offering_axe_removes_item_via_beat(player):
    player.add_item("Gunnar's Axe")
    apply_choice("offering_scene", "0", player)  # choose axe
    render_scene("offered_axe_scene", player)
    assert "Gunnar's Axe" not in player.inventory


def test_offering_axe_sets_flag_and_honour(player):
    player.add_item("Gunnar's Axe")
    apply_choice("offering_scene", "0", player)
    assert player.has_flag("offered_axe")
    assert player.honour == 60  # default 50 + 10


def test_offering_pelt_removes_item_via_beat(player):
    player.add_item("bear pelt")
    apply_choice("offering_scene", "0", player)  # bear pelt is choice 0 without axe
    render_scene("offered_pelt_scene", player)
    assert "bear pelt" not in player.inventory


def test_offering_pelt_sets_flag(player):
    player.add_item("bear pelt")
    apply_choice("offering_scene", "0", player)
    assert player.has_flag("offered_pelt")


def test_interior_reacts_to_axe_offering(player):
    player.set_flag("offered_axe")
    out = render_scene("interior_scene", player)
    texts = [p["text"] for p in out["paragraphs"]]
    assert "He sees your empty hand." in texts


def test_interior_reacts_to_pelt_offering(player):
    player.set_flag("offered_pelt")
    out = render_scene("interior_scene", player)
    texts = [p["text"] for p in out["paragraphs"]]
    assert "He glances toward the door." in texts


def test_interior_no_reaction_without_offering(player):
    out = render_scene("interior_scene", player)
    texts = [p["text"] for p in out["paragraphs"]]
    assert "He sees your empty hand." not in texts
    assert "He glances toward the door." not in texts


# ── has_prose_beats ───────────────────────────────────────────


def test_has_prose_beats_true_for_prose():
    assert has_prose_beats([{"type": "prose", "text": "x"}]) is True


def test_has_prose_beats_true_for_italic():
    assert has_prose_beats([{"type": "italic", "text": "x"}]) is True


def test_has_prose_beats_true_for_memory():
    assert (
        has_prose_beats([{"type": "memory", "key": "k", "label": "l", "text": "x"}])
        is True
    )


def test_has_prose_beats_true_for_conditional_prose():
    assert has_prose_beats([{"type": "conditional_prose", "variants": []}]) is True


def test_has_prose_beats_false_for_stat_only():
    assert has_prose_beats([{"type": "stat", "changes": {"honour": 5}}]) is False


def test_has_prose_beats_false_for_empty():
    assert has_prose_beats([]) is False


def test_has_prose_beats_mixed_returns_true():
    beats = [
        {"type": "flag", "key": "x"},
        {"type": "prose", "text": "y"},
    ]
    assert has_prose_beats(beats) is True


# ── _build_hud ────────────────────────────────────────────────


def test_build_hud_hp_values(player):
    player.health = 60
    hud = _build_hud(player)
    assert hud["hp"] == 60
    assert hud["max_hp"] == 100
    assert hud["hp_ratio"] == 0.6


def test_build_hud_hp_desc_unbroken(player):
    player.health = 100
    hud = _build_hud(player)
    assert hud["hp_desc"] == "Unbroken"


def test_build_hud_hp_desc_wounded(player):
    player.health = 60
    hud = _build_hud(player)
    assert hud["hp_desc"] == "Wounded"


def test_build_hud_hp_desc_near_death(player):
    player.health = 10
    hud = _build_hud(player)
    assert hud["hp_desc"] == "Near Death"


def test_build_hud_is_dead_false(player):
    hud = _build_hud(player)
    assert hud["is_dead"] is False


def test_build_hud_is_dead_true(player):
    player.health = 0
    hud = _build_hud(player)
    assert hud["is_dead"] is True


def test_build_hud_shards(player):
    player.echo_shards = 150
    hud = _build_hud(player)
    assert hud["shards"] == 150


# ── apply_choice narration ────────────────────────────────────


def test_apply_choice_narration_none_by_default(player):
    _, narration = apply_choice("apply_choice_scene", "0", player)
    assert narration is None


def test_apply_choice_remove_item_via_field(player):
    player.add_item("iron scraps")
    apply_choice("choice_remove_item_scene", "0", player)
    assert "iron scraps" not in player.inventory
