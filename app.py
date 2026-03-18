# ============================================================
#  app.py — Forgotten Among the Fallen
#  Flask web server. Run: python app.py
#  Requires: pip install flask
# ============================================================
from flask import Flask, render_template, jsonify, request, session
import json, os, uuid

from engine.state     import PlayerState
from engine.scene_web import render_scene, apply_choice, _build_hud
from engine.combat_web import (
    ENEMIES, start_combat, get_player_actions,
    resolve_action
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "forgotten-among-the-fallen-dev-key")

# ── Session helpers ───────────────────────────────────────────

def _get_state() -> PlayerState:
    data = session.get("state")
    if data:
        return PlayerState.from_dict(data)
    return PlayerState()

def _save_state(state: PlayerState):
    session["state"] = state.to_dict()
    session.modified = True

def _get_combat() -> dict | None:
    raw = session.get("combat")
    if raw:
        return json.loads(raw)
    return None

def _save_combat(combat: dict | None):
    if combat is None:
        session.pop("combat", None)
    else:
        session["combat"] = json.dumps(combat)
    session.modified = True

# ═══════════════════════════════════════════════════════════
#  ROUTES
# ═══════════════════════════════════════════════════════════

@app.route("/")
def index():
    return render_template("index.html")

# ── New game ──────────────────────────────────────────────────
@app.route("/api/new", methods=["POST"])
def new_game():
    state = PlayerState()
    state.current_scene = "awakening"
    _save_state(state)
    _save_combat(None)
    return jsonify({"ok": True})

# ── Load current scene ────────────────────────────────────────
@app.route("/api/scene", methods=["GET"])
def get_scene():
    state = _get_state()
    if not state.current_scene:
        state.current_scene = "awakening"

    key = state.current_scene

    # Handle special keys
    if key in ("__save_quit__", "end", "__end__"):
        return jsonify({"game_over": True, "credits": True})

    if key == "__restart__":
        state = PlayerState()
        state.current_scene = "awakening"
        _save_state(state)
        key = "awakening"

    # Auto-advance through chain scenes (scenes with only 'next', no choices)
    # Limit to 10 hops to prevent infinite loops
    from content.scenes import SCENES
    hops = 0
    while hops < 10:
        if key not in SCENES:
            break
        scene = SCENES[key]
        has_choices = bool(scene.get("choices"))
        has_next    = bool(scene.get("next"))
        has_combat  = any(b.get("type") == "combat" for b in scene.get("beats", []))
        has_input   = any(b.get("type") == "input"  for b in scene.get("beats", []))
        # Only auto-advance if purely a passthrough (next only, no choices, no combat, no input)
        if has_next and not has_choices and not has_combat and not has_input:
            # Render the scene beats for side effects, then advance
            output = render_scene(key, state)
            _save_state(state)
            key = scene["next"]
            state.current_scene = key
            hops += 1
        else:
            break

    output = render_scene(key, state)
    _save_state(state)

    # If scene triggers combat, initialise it
    if output.get("combat"):
        enemy_key    = output["combat"]["enemy_key"]
        combat_state = start_combat(enemy_key, state)
        _save_combat(combat_state)
        _save_state(state)
        output["combat"]["actions"]         = get_player_actions(combat_state, state)
        output["combat"]["enemy_name"]      = ENEMIES[enemy_key]["name"]
        output["combat"]["enemy_hp_ratio"]  = (
            combat_state["enemy"]["current_hp"] / combat_state["enemy"]["hp"]
        )
        output["combat"]["log"] = combat_state["log"]

    return jsonify(output)

# ── Make a choice ─────────────────────────────────────────────
@app.route("/api/choose", methods=["POST"])
def choose():
    data      = request.get_json()
    choice_id = data.get("choice_id", "0")
    state     = _get_state()
    scene_key = state.current_scene

    # Handle name input specially
    if data.get("name"):
        state.name = data["name"].strip() or "the drengr"
        # Skip name prompt, advance to next scene
        from content.scenes import SCENES
        scene = SCENES.get(scene_key, {})
        choices = scene.get("choices", [])
        if choices:
            next_key = apply_choice(scene_key, "0", state)
        else:
            next_key = scene.get("next", "battlefield_open")
        state.current_scene = next_key
        _save_state(state)
        return jsonify({"next_scene": next_key, "ok": True})

    next_key = apply_choice(scene_key, choice_id, state)

    # Handle special destinations
    if next_key == "__save_quit__":
        state.save(0)
        _save_state(state)
        return jsonify({"game_over": True})

    state.current_scene = next_key
    state.visited.append(scene_key)
    state.save(0)
    _save_state(state)
    return jsonify({"next_scene": next_key, "ok": True})

# ── Combat action ─────────────────────────────────────────────
@app.route("/api/combat/action", methods=["POST"])
def combat_action():
    data      = request.get_json()
    action_id = data.get("action_id")
    state     = _get_state()
    combat    = _get_combat()

    if not combat:
        return jsonify({"error": "No active combat"}), 400

    combat = resolve_action(action_id, combat, state)
    _save_state(state)

    response = {
        "log":          combat["log"][-6:],  # last 6 entries
        "over":         combat["over"],
        "won":          combat.get("won", False),
        "fled":         combat.get("fled", False),
        "died":         combat.get("died", False),
        "hud":          _build_hud(state),
        "enemy_hp_ratio": (
            combat["enemy"]["current_hp"] / combat["enemy"]["hp"]
            if combat["enemy"]["hp"] > 0 else 0
        ),
        "shards_gained": combat.get("shards_gained", 0),
        "items_gained":  combat.get("items_gained", []),
    }

    if not combat["over"]:
        response["actions"] = get_player_actions(combat, state)
        _save_combat(combat)
    else:
        _save_combat(None)
        # Advance past the combat scene
        state.current_scene = _advance_after_combat(
            state.current_scene, combat
        )
        state.save(0)
        _save_state(state)
        response["next_scene"] = state.current_scene

    return jsonify(response)

# ── Status ────────────────────────────────────────────────────
@app.route("/api/status", methods=["GET"])
def status():
    state = _get_state()
    return jsonify({
        "has_save":     os.path.exists("saves/save_0.json"),
        "scene":        state.current_scene,
        "curse":        state.curse_stacks,
        "shards":       state.echo_shards,
        "memories":     state.memories,
        "inventory":    state.inventory,
        "deaths":       state.deaths,
    })

@app.route("/api/advance", methods=["POST"])
def advance():
    """Advance to a known next scene (used by auto-next scenes with no choices)."""
    data     = request.get_json()
    next_key = data.get("next_scene", "")
    state    = _get_state()

    if next_key in ("__save_quit__", "end", "__end__"):
        state.save(0)
        _save_state(state)
        return jsonify({"game_over": True})

    if next_key == "__restart__":
        state = PlayerState()
        next_key = "awakening"

    state.current_scene = next_key
    state.save(0)
    _save_state(state)
    return jsonify({"ok": True, "next_scene": next_key})


def load_game():
    state = PlayerState.load(0)
    if state is None:
        return jsonify({"error": "No save found"}), 404
    _save_state(state)
    _save_combat(None)
    return jsonify({"ok": True, "scene": state.current_scene})

# ── Helpers ───────────────────────────────────────────────────

def _advance_after_combat(scene_key: str, combat: dict) -> str:
    """After combat ends, move to the right next scene."""
    if combat.get("died"):
        return scene_key  # respawn in same scene
    # Map combat scenes to their post-combat destinations
    post_combat = {
        "combat_draugar_east": "scavenge_east_after",
        "combat_gunnar":       "zone_1_end",
    }
    if combat.get("fled"):
        return "battlefield_open"
    return post_combat.get(scene_key, "battlefield_open")

# ═══════════════════════════════════════════════════════════
#  ENTRY
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    os.makedirs("saves", exist_ok=True)
    print("\n  Forgotten Among the Fallen")
    print("  Open: http://localhost:5000\n")
    app.run(debug=True, port=5000)
