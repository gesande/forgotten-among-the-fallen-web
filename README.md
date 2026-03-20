# Forgotten Among the Fallen

A dark fantasy Viking experience set in a desolate world between life and death.

Beneath a silent, star-filled sky, fallen warriors lie forgotten — but not at rest.
Ancient runes still burn in the earth, and something stirs beneath the fog.

Explore a cursed battlefield where time has no meaning, uncover remnants of a lost world,
and face forces that should not exist.

## Features

- Atmospheric dark fantasy setting inspired by Norse myth and liminal spaces
- Desolate environments shaped by war, ruin, and silence
- Runic elements and subtle supernatural presence
- Cinematic visual tone with painterly aesthetics

## Vision

A slow, immersive experience focused on mood, isolation, and the boundary between life and death.

## Setup

```bash
pip install flask
python app.py
```

Then open: http://localhost:5000

## Structure

```
app.py                  ← Flask server + API routes
requirements.txt        ← pip install flask

engine/
  state.py              ← PlayerState (unchanged from terminal version)
  scene_web.py          ← Scene runner returning JSON
  combat_web.py         ← Combat engine returning JSON

content/
  scenes.py             ← All 27 scenes (unchanged)

static/
  css/game.css          ← Full dark fantasy stylesheet
  js/game.js            ← Frontend game controller
  svg/
    battlefield.svg     ← The Waking Field
    leif.svg            ← The Dying Soldier
    longhouse.svg       ← Longhouse Ruins + Ghost-Forge
    cairn.svg           ← The Bone Cairn
    mound.svg           ← Mound of Oathbreakers
    gunnar.svg          ← Gunnar the Hollow King
    scavenge.svg        ← The Dense Dead
    combat_draugar.svg  ← Combat scene

templates/
  index.html            ← Single-page game shell

saves/                  ← Auto-created, JSON save files
```

## API Endpoints

| Method | Route              | Description                         |
|--------|--------------------|-------------------------------------|
| POST   | /api/new           | Start a new game                    |
| POST   | /api/load          | Load save slot 0                    |
| GET    | /api/scene         | Get current scene (rendered JSON)   |
| POST   | /api/choose        | Make a choice `{choice_id}`         |
| POST   | /api/combat/action | Execute combat action `{action_id}` |
| GET    | /api/status        | Save state summary                  |

## Adding scenes

Edit `content/scenes.py` — the engine picks them up automatically.
Add a new SVG to `static/svg/` and map it in `engine/scene_web.py`.
