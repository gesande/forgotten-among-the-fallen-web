# ============================================================
#  engine/scene_web.py
#  Scene runner for the web version.
#  Instead of printing, returns a SceneOutput dict:
#  {
#    "scene_key": str,
#    "art_key":   str,          # which SVG illustration to show
#    "header":    {title, subtitle} | None,
#    "beats":     [ {type, text, ...} ],   # rendered narrative
#    "choices":   [ {id, label} ],
#    "hud":       {hp, stamina, wrath, curse, shards, hp_desc},
#    "combat":    None | {enemy_key},      # triggers combat mode
#    "next":      str | None,              # auto-advance scene
#  }
# ============================================================
from engine.state import PlayerState
from content.scenes import SCENES

# ── Art key mapping — which SVG to show per scene ────────────
SCENE_ART = {
    "name_entry":               "name_entry",
    "awakening":                "battlefield",
    "find_weapon":              "battlefield",
    "battlefield_open":         "battlefield",
    "battlefield_look_around":  "battlefield",
    "soul_leif":                "leif",
    "leif_gives_name":          "leif",
    "leif_the_oath":            "leif",
    "leif_gunnar_intro":        "leif",
    "leif_farewell":            "leif",
    "leif_mercy_kill":          "leif",
    "leif_defense":             "leif",
    "leif_battle_account":      "leif",
    "leif_survivors":           "leif",
    "longhouse_ruins":          "longhouse",
    "cairn_rest":               "cairn",
    "forge_search":             "longhouse",
    "scavenge_east":            "scavenge",
    "scavenge_east_after":      "scavenge",
    "combat_draugar_east":      "combat_draugar",
    "the_mound":                "mound",
    "gunnar_dialogue_peace":    "gunnar",
    "gunnar_dialogue_challenge":"gunnar",
    "gunnar_dialogue_truth":    "gunnar",
    "combat_gunnar":            "gunnar_combat",
    "zone_1_end":               "mound",
    "final_rest":               "cairn",
    "act_2_intro":              "act_break",
    # Act II — The Stirring Beneath
    "fog_road":                 "fog_road",
    "fog_the_held":             "fog_road",
    "fog_held_other":           "fog_road",
    "fog_held_release":         "fog_road",
    "fog_held_after":           "fog_road",
    "fog_sentinel":             "fog_sentinel",
    "fog_sentinel_wait":        "fog_sentinel",
    "fog_sentinel_avoided":     "fog_sentinel",
    "combat_fog_sentinel":      "fog_sentinel",
    "fog_sentinel_after":       "fog_road",
    "gatehouse_approach":       "gatehouse",
    "gatehouse_guards":         "gatehouse",
    "gatehouse_courtyard":      "gatehouse",
    "gatehouse_wall":           "gatehouse",
    "gatehouse_inside":         "gatehouse",
    # Act II — The Great Hall / Odrik
    "great_hall_entrance":      "great_hall",
    "odrik_silence":            "great_hall",
    "odrik_knew":               "great_hall",
    "odrik_what_are_you":       "great_hall",
    "odrik_measures_you":       "great_hall",
    "odrik_first_questions":    "great_hall",
    "odrik_explains_place":     "great_hall",
    "odrik_the_night":          "great_hall",
    "odrik_the_key":            "great_hall",
    "odrik_why_bound":          "great_hall",
}

def render_scene(scene_key: str, state: PlayerState) -> dict:
    """
    Process a scene and return a structured dict for the frontend.
    Side-effects (items, stats, flags, shards, heal) only apply on
    the first visit — subsequent loads are display-only.
    """
    if scene_key not in SCENES:
        return {"error": f"Unknown scene: {scene_key}"}

    # Track whether this is the first time we're processing this scene
    visited_key = f"scene_visited_{scene_key}"
    first_visit = not state.has_flag(visited_key)
    if first_visit:
        state.set_flag(visited_key, True)

    scene   = SCENES[scene_key]
    output  = {
        "scene_key": scene_key,
        "art_key":   SCENE_ART.get(scene_key, "battlefield"),
        "header":    scene.get("header"),
        "paragraphs":[],      # rendered narrative text blocks
        "memories":  [],      # any memories recovered this scene
        "items":     [],      # items gained
        "shards":    0,       # shards gained
        "choices":   [],
        "next":      None,
        "combat":    None,    # set if a combat beat triggers
        "hud":       _build_hud(state),
        "name_prompt": False, # set True if scene wants player name
    }

    # ── Process beats ─────────────────────────────────────────
    for beat in scene.get("beats", []):
        _process_beat(beat, state, output, first_visit)
        # Stop processing beats once combat is triggered
        if output["combat"]:
            break

    # ── Build choices ─────────────────────────────────────────
    if not output["combat"]:
        raw_choices = scene.get("choices", [])
        filtered_idx = 0
        for i, c in enumerate(raw_choices):
            cond = c.get("condition")
            if cond and not cond(state):
                continue
            output["choices"].append({
                "id":    str(filtered_idx),
                "label": c["label"],
            })
            filtered_idx += 1

        # If no choices and no next — check if this was a pure combat scene
        # whose combat was skipped (already defeated). Auto-advance via backend.
        all_combat = all(
            b.get("type") == "combat"
            for b in scene.get("beats", [])
            if b.get("type") not in ("flag", "stat")
        )
        if not raw_choices and not scene.get("next") and all_combat:
            # Combat already resolved — signal frontend to call /api/advance
            output["combat_resolved"] = True

        if not raw_choices and scene.get("next"):
            # Only auto-advance (no Continue button) if scene has no prose to show
            has_prose  = any(
                b.get("type") in ("prose", "italic", "memory", "conditional_prose")
                for b in scene.get("beats", [])
            )
            has_input  = any(b.get("type") == "input" for b in scene.get("beats", []))
            if has_prose and not has_input:
                # Has prose but no input — show Continue button
                output["choices"] = [{"id": "__next__", "label": "Continue"}]
            elif not has_prose:
                output["next"] = scene["next"]
            # If has_input: name field acts as the continue — no extra button needed

    # Refresh HUD after beat effects
    output["hud"] = _build_hud(state)
    return output

def apply_choice(scene_key: str, choice_id: str, state: PlayerState) -> str:
    """
    Apply the effects of a chosen option and return the next scene key.
    """
    scene   = SCENES[scene_key]
    choices = scene.get("choices", [])
    # Filter to available choices, same as render_scene
    available = []
    for c in choices:
        cond = c.get("condition")
        if cond and not cond(state):
            continue
        available.append(c)

    idx = int(choice_id)
    if idx >= len(available):
        return scene_key  # safety fallback

    choice = available[idx]

    # Apply stat effects
    for stat, delta in choice.get("effects", {}).items():
        state.modify_stat(stat, delta)
    # Apply flags
    for flag, val in choice.get("flags", {}).items():
        state.set_flag(flag, val)
    # Apply items
    if choice.get("item"):
        state.add_item(choice["item"])
    # Apply shards
    if choice.get("shards"):
        state.echo_shards += choice["shards"]
    # Apply heal
    if choice.get("heal"):
        state.heal(choice["heal"])

    return choice.get("next", "end"), choice.get("narration")

# ── Beat processor ────────────────────────────────────────────

def _process_beat(beat: dict, state: PlayerState, output: dict, first_visit: bool = True) -> None:
    kind = beat.get("type", "prose")

    # Condition gate
    cond = beat.get("condition")
    if cond and not cond(state):
        return

    if kind == "prose":
        output["paragraphs"].append({"type": "prose", "text": beat["text"]})

    elif kind == "italic":
        output["paragraphs"].append({"type": "italic", "text": beat["text"]})

    elif kind == "memory":
        key   = beat.get("key", "memory")
        label = beat.get("label", "")
        if state.add_memory(key, label):  # add_memory is already idempotent
            output["memories"].append(beat["text"])
            output["paragraphs"].append({
                "type": "memory",
                "text": beat["text"],
                "label": label,
            })

    elif kind == "conditional_prose":
        for variant in beat.get("variants", []):
            vcond = variant.get("condition")
            if vcond is None or vcond(state):
                output["paragraphs"].append({"type": "prose", "text": variant["text"]})
                break

    elif kind == "combat":
        enemy_key = beat["enemy"]
        flag      = beat.get("flag", f"defeated_{enemy_key}")
        if not state.has_flag(flag):
            output["combat"] = {"enemy_key": enemy_key}

    # ── Side-effects below only apply on first visit ──────────
    elif kind == "stat":
        if first_visit:
            for stat, delta in beat.get("changes", {}).items():
                state.modify_stat(stat, delta)

    elif kind == "flag":
        if first_visit:
            state.set_flag(beat["key"], beat.get("value", True))

    elif kind == "item":
        if first_visit:
            item   = beat["item"]
            action = beat.get("action", "give")
            if action == "give":
                state.add_item(item)
                output["items"].append(item)
            elif action == "take":
                state.remove_item(item)

    elif kind == "shards":
        if first_visit:
            amount = beat["amount"]
            state.echo_shards = max(0, state.echo_shards + amount)
            output["shards"] += amount

    elif kind == "heal":
        if first_visit:
            amount = beat.get("amount", state.max_health)
            state.heal(amount)

    elif kind == "input":
        if beat.get("store_as") == "name":
            output["name_prompt"] = True

# ── HUD builder ───────────────────────────────────────────────

def _build_hud(state: PlayerState) -> dict:
    hp_ratio = state.health / state.max_health
    if hp_ratio > 0.75:   hp_desc = "Unbroken"
    elif hp_ratio > 0.50: hp_desc = "Wounded"
    elif hp_ratio > 0.25: hp_desc = "Bleeding"
    else:                 hp_desc = "Near Death"

    return {
        "hp":         state.health,
        "max_hp":     state.max_health,
        "hp_ratio":   hp_ratio,
        "hp_desc":    hp_desc,
        "wrath":      state.wrath,
        "max_wrath":  state.max_wrath if hasattr(state, "max_wrath") else 100,
        "curse":      state.curse_stacks,
        "shards":     state.echo_shards,
        "memories":   len(state.memories),
        "inventory":  state.inventory,
        "is_dead":    state.is_dead(),
        "is_cursed":  state.is_cursed(),
    }
