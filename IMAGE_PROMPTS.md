# Forgotten Among the Fallen — Image Generation Prompts

Save generated images as **1600×900px** (16:9) JPG or PNG.
Replace the SVG files in `static/svg/` — just change the `<img>` src
extension in `templates/index.html` from `.svg` to `.jpg` (or `.png`).

---

## Style Reference (add to ALL prompts)

**Midjourney suffix** — paste after every prompt:
```
--ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion suffix** — add to every positive prompt:
```
cinematic lighting, volumetric fog, dark fantasy, muted desaturated palette,
oil painting texture, 8k, highly detailed, masterpiece
```

**Negative prompt (SD)** — add to all:
```
bright colors, cartoon, anime, modern, guns, sci-fi, text, watermark,
oversaturated, HDR, lens flare, purple sky
```

---

## Scene 1 — battlefield.jpg
**File:** `static/svg/battlefield.svg` → replace with `battlefield.jpg`

**Midjourney:**
```
a vast dark viking battlefield after a total mutual annihilation, ten thousand
bodies lying in deep mud under a heavy bruise-colored sky, no survivors, no
crows, broken spears driven into the earth at strange angles, distant jagged
mountains barely visible through thick grey fog, one pale crescent moon, cold
iron light, pre-dawn, dark fantasy, painterly, desaturated, Erik the Viking
aesthetic --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
vast viking battlefield after battle, mutual annihilation, ten thousand corpses
in mud, broken shields, spears in ground, pale crescent moon, heavy fog, bruise
colored sky, no survivors, cold iron light, dark fantasy, muted palette
```

---

## Scene 2 — leif.jpg
**File:** `static/svg/leif.svg` → replace with `leif.jpg`

**Midjourney:**
```
a dying viking warrior sitting against a shattered wooden shield-wall in deep
mud, arrow through his side, looking upward with calm resigned eyes, faint
torchlight from the left, darkness all around, mist rising from the ground,
dark fantasy portrait, painterly, desaturated earth tones, detailed armor,
chainmail worn and bloodied --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
dying viking warrior sitting against broken shield wall, arrow in side, calm
expression looking up, torchlight, ground mist, dark mud, chainmail armor,
dark fantasy, muted tones, painterly, cinematic
```

---

## Scene 3 — longhouse.jpg
**File:** `static/svg/longhouse.svg` → replace with `longhouse.jpg`

**Midjourney:**
```
ruins of a collapsed viking longhouse at night, interior view, heavy timber
beams fallen inward, a blacksmith forge still glowing faintly with dying embers
in the center, a small bone cairn with rune carvings faintly lit nearby, cold
moonlight through collapsed roof, ash and dust in the air, dark fantasy,
painterly, desolate atmosphere --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
collapsed viking longhouse interior at night, fallen timber beams, blacksmith
forge with dying embers, bone cairn with glowing runes, moonlight through roof,
ash and dust, dark fantasy, desolate, painterly, muted palette
```

---

## Scene 4 — cairn.jpg
**File:** `static/svg/cairn.svg` → replace with `cairn.jpg`

**Midjourney:**
```
a single ancient bone cairn made of dark stacked stones in the middle of a dark
battlefield at night, runes carved into the stones glowing faintly amber-gold,
warm fire burning inside through carved gaps, cold stars above, mist rolling
across the ground, still air, the only light source, dark fantasy, painterly,
intimate, sacred atmosphere --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
ancient bone cairn stacked dark stones at night, glowing amber runes carved
into stone, warm fire inside, cold starfield, ground mist, only light source,
dark fantasy, sacred, painterly, cinematic lighting
```

---

## Scene 5 — mound.jpg
**File:** `static/svg/mound.svg` → replace with `mound.jpg`

**Midjourney:**
```
a large ancient burial mound at night covered in grave markers, tilted wooden
crosses and carved standing stones, the disturbed earth darker than the
surroundings, oppressive purple-grey sky, thin fog crawling at the base, a
feeling of profound unease, no figures visible, dark fantasy, painterly,
ominous, prehistoric burial site, cursed ground --ar 16:9 --style raw --v 6
--stylize 800
```

**Stable Diffusion:**
```
ancient viking burial mound at night, grave markers and tilted crosses, dark
disturbed earth, oppressive purple grey sky, ground fog, no figures, ominous,
cursed ground, dark fantasy, painterly, muted desaturated palette
```

---

## Scene 6 — gunnar.jpg
**File:** `static/svg/gunnar.svg` → replace with `gunnar.jpg`

**Midjourney:**
```
a towering undead viking commander standing on a burial mound at night, heavy
battered plate armor, a great axe held at his side, eyes glowing cold blue-
white, spectral purple aura around him, face obscured by a cracked horned
helmet, ground mist at his feet, a presence that is wrong, that should not be
standing, dark fantasy boss character, painterly, cinematic, extremely
atmospheric --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
undead viking commander on burial mound night, heavy battered plate armor,
great axe, glowing cold blue eyes, spectral purple aura, cracked helmet,
ground mist, wrong presence, dark fantasy boss, painterly, cinematic, detailed
```

---

## Scene 7 — scavenge.jpg
**File:** `static/svg/scavenge.svg` → replace with `scavenge.jpg`

**Midjourney:**
```
dense carpet of fallen viking warriors after a battle, bodies piled two and
three deep, broken weapons and shields everywhere, fog so thick the far end
disappears, one arm beginning to rise from the pile of dead, glowing eye
visible in the dark, horrifying implication of the dead awakening, dark
fantasy, painterly, desaturated, body horror atmosphere --ar 16:9 --style raw
--v 6 --stylize 800
```

**Stable Diffusion:**
```
dense battlefield dead vikings bodies piled in mud, broken weapons shields,
thick fog, one arm rising from pile, glowing eye in darkness, dead awakening,
dark fantasy, body horror, painterly, desaturated, cinematic
```

---

## Scene 8 — combat_draugar.jpg
**File:** `static/svg/combat_draugar.svg` → replace with `combat_draugar.jpg`

**Midjourney:**
```
a viking warrior facing an undead draugar in close combat on a dark
battlefield, the warrior raising a war axe with a glowing rune on the blade,
the draugar with hollow glowing dead eyes and rusted weapons, both figures
silhouetted against thin cold moonlight, fog at knee height, sparks between
weapons, dark fantasy, action, painterly, cinematic --ar 16:9 --style raw --v 6
--stylize 800
```

**Stable Diffusion:**
```
viking warrior vs undead draugar close combat, rune axe glowing, hollow dead
eyes, moonlit battlefield silhouettes, fog, weapon sparks, dark fantasy,
action, painterly, cinematic, detailed armor
```

---

## Scene 9 — act_break.jpg
**File:** `static/svg/act_break.svg` → replace with `act_break.jpg`

**Midjourney:**
```
an infinite starfield over a frozen nordic landscape, distant jagged mountains
with snow, a single thin beam of runic light rising from the ground into the
sky, absolute silence, the feeling of standing between worlds, between life and
death, vast and cold, dark fantasy, painterly, cosmic, liminal space --ar 16:9
--style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
infinite starfield frozen nordic landscape, jagged snow mountains, thin runic
light beam rising from ground, absolute silence, between worlds liminal space,
vast cold dark, dark fantasy, painterly, cosmic atmosphere
```

---

## How to swap in generated images

1. Generate each image and save to `static/svg/` (yes, same folder is fine,
   or create `static/img/` if you prefer)

2. In `engine/scene_web.py`, the `SCENE_ART` dict maps scene keys to art keys.
   The frontend loads `/static/svg/{art_key}.svg` — just change the base path
   and extension in `static/js/game.js`:

   ```js
   // Change this line in game.js:
   const ART_BASE = "/static/svg/";
   // To:
   const ART_BASE = "/static/img/";
   ```

   And update the extension check in `renderScene()`:
   ```js
   artEl.src = `${ART_BASE}${artKey}.jpg`;
   ```

3. The SVG fallback system remains — if an image fails to load it falls
   back to `battlefield.jpg` automatically.

---

## Music file names expected

Place audio files in `static/audio/` and `static/audio/`.
The engine tries `.ogg` first, then `.mp3`.

---

## Act II — The Stirring Beneath

---

## Scene 10 — fog_road.jpg
**File:** `static/svg/fog_road.svg` → replace with `fog_road.jpg`
**Used in:** fog_road, fog_the_held, fog_held_release, fog_held_after, fog_sentinel_after

**Midjourney:**
```
a narrow ancient stone road disappearing into impenetrable white-grey fog, deep
mud on both sides, the road barely visible beyond ten feet, two small human
figures standing motionless in the middle distance facing each other as if
frozen mid-conversation, thick fog consuming everything above waist height,
cold diffuse light with no visible source, dark fantasy, painterly, completely
desaturated, liminal, purgatorial atmosphere, no sky visible, silent
--ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
ancient stone road into thick fog, two figures frozen mid-conversation in
distance, deep mud, no sky, cold diffuse light, desaturated, dark fantasy,
painterly, liminal purgatorial atmosphere, silent, cinematic
```

---

## Scene 11 — fog_sentinel.jpg
**File:** `static/svg/fog_sentinel.svg` → replace with `fog_sentinel.jpg`
**Used in:** fog_sentinel, fog_sentinel_wait, combat_fog_sentinel

**Midjourney:**
```
a towering impossibly thin humanoid figure standing motionless in the center
of a fog-shrouded road, proportions deeply wrong — too narrow, arms hanging
far too low, no visible face, whole body like a dark post driven into the
earth, thick white fog curling around it as if the fog belongs to it, cold
bluish-white light emanating faintly from where a face should be, dark
fantasy horror, painterly, desaturated, deeply unsettling stillness,
bell jar atmosphere --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
impossibly thin tall humanoid figure on foggy road, wrong proportions arms
too long, no face, fog curling around it possessively, faint cold blue-white
glow, dark fantasy horror, deeply unsettling, painterly, desaturated,
cinematic, purgatorial
```

---

## Scene 12 — gatehouse.jpg
**File:** `static/svg/gatehouse.svg` → replace with `gatehouse.jpg`
**Used in:** gatehouse_approach, gatehouse_guards, gatehouse_courtyard, gatehouse_wall, gatehouse_inside

**Midjourney:**
```
a fortified viking gatehouse seen from outside at night, both heavy wooden
doors standing fully open as if welcoming, two armored guards standing
perfectly still at their posts not breathing, a single torch burning at
the top of the stone tower, thick fog pressing against the walls but not
entering, warm orange torchlight against cold grey stone, a horse saddled
and waiting at a hitching post just inside the gate, dark fantasy, painterly,
desaturated, deeply wrong stillness, something held rather than abandoned
--ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
viking stone gatehouse at night, doors open wide, two guards standing
perfectly still not breathing, single torch on tower, thick fog outside
walls, warm torchlight cold stone, horse saddled waiting inside, dark
fantasy, painterly, desaturated, unsettling stillness, cinematic
```

---

### Music tracks
| Filename                  | Scene              | Mood                                    |
|---------------------------|--------------------|-----------------------------------------|
| `ambient_title.ogg`       | Title screen       | Slow dark Norse ambient, builds slowly  |
| `ambient_leif.ogg`        | Leif scenes        | Slow sorrowful strings, melancholic    |
| `ambient_battlefield.ogg` | Battlefield        | Slow wind, distant horn, no melody     |
| `ambient_forge.ogg`       | Longhouse          | Low hum, crackling fire, bass drone    |
| `ambient_cairn.ogg`       | Bone Cairn         | Ethereal, rune tones, sparse           |
| `ambient_mound.ogg`       | The Mound          | Oppressive bass drone, silence breaks  |
| `ambient_void.ogg`        | Act break          | Near silence, one distant horn note    |
| `ambient_fog_road.ogg`    | Fog road / The Held | Slow breathing rhythm, no melody, warm but wrong |
| `ambient_gatehouse.ogg`   | Gatehouse          | Complete silence broken by single creak or drip |
| `combat_draugar.ogg`      | Draugar combat     | Urgent percussion, no melody           |
| `combat_boss.ogg`         | Gunnar boss fight  | War drums, heavy, relentless           |
| `combat_sentinel.ogg`     | Fog-sentinel fight | Single sustained bell tone, slow pulse, no percussion |

### SFX
| Filename          | Trigger                    |
|-------------------|----------------------------|
| `sfx_choice.ogg`  | Hover over choice button   |
| `sfx_confirm.ogg` | Click a choice             |
| `sfx_memory.ogg`  | Memory fragment recovered  |
| `sfx_death.ogg`   | Player falls in combat     |
| `sfx_shards.ogg`  | Echo shards gained         |
| `sfx_hit.ogg`     | Combat hit lands           |
| `sfx_miss.ogg`    | Combat attack misses       |
| `sfx_parry.ogg`   | Parry succeeds             |

### Recommended Suno/Udio prompts for music
- **ambient_title**: "dark norse atmospheric intro, slow building tension, distant
  single horn note fading in, deep silence between sounds, title screen atmosphere,
  no melody, no percussion, 3 minutes loop"
- **ambient_leif**: "slow sorrowful norse ambient, single cello or low strings,
  sparse melody, dying soldier atmosphere, melancholic but not hopeless,
  quiet and intimate, no percussion, 3 minutes loop"
- **ambient_battlefield**: "dark norse ambient, wind howling, distant war horn,
  slow deep drums fading in and out, no melody, 3 minutes, loop"
- **ambient_forge**: "dark medieval blacksmith ambient, dying forge embers crackling,
  low resonant drone, occasional distant hammer strike on metal, warm but desolate,
  sacred atmosphere, no melody, 3 minutes loop"
- **ambient_cairn**: "ethereal norse ambient, singing bowls, rune tones,
  sparse, sacred feeling, very quiet, 3 minutes loop"
- **ambient_mound**: "oppressive dark norse drone, deep bass rumble, burial mound
  atmosphere, silence punctuated by distant wind, ominous, no melody, no percussion,
  unsettling, 3 minutes loop"
- **ambient_void**: "near silence dark ambient, single distant viking horn note,
  vast empty space, cold wind, between worlds liminal atmosphere, very minimal,
  90 seconds loop"
- **combat_draugar**: "viking battle percussion, urgent rhythmic drums, no
  melody, intense, dark, 90 seconds loop"
- **combat_boss**: "epic dark norse boss fight music, heavy war drums, chanting,
  ominous, relentless tempo, 2 minutes loop"

### Recommended prompts for SFX
- **sfx_choice**: "soft parchment rustling, quiet, subtle, ui hover sound"
- **sfx_confirm**: "heavy iron click, satisfying, medieval, selection confirm sound"
- **sfx_memory**: "ethereal frost bell chime, single note, reverb, memory recovered"
- **sfx_death**: "deep resonant iron toll, single heavy bell, slow decay, death knell"
- **sfx_shards**: "crystalline ice shards clinking, bright, magical, short"
- **sfx_hit**: "iron on iron impact, heavy, combat hit, short sharp"
- **sfx_miss**: "weapon swoosh through air, short, combat miss"
- **sfx_parry**: "ringing metal clash, iron parry, short bright tone, success sound"

---

## Act II — Audio additions

### New music tracks
- **ambient_fog_road**: "slow rhythmic breathing sound as ambient music, warm but
  deeply wrong temperature, no instruments, fog atmosphere, purgatorial, something
  inhuman exhaling slowly, liminal dread, 3 minutes loop"
- **ambient_gatehouse**: "complete interior silence ambient, single drop of water
  echoing in stone chamber, occasional distant creak of heavy wood, held breath
  atmosphere, warmth without comfort, 3 minutes loop"
- **combat_sentinel**: "single sustained low bell tone pulsing slowly, no percussion
  no melody, the bell never fully decays, something absorbing sound, combat
  atmosphere without urgency, 90 seconds loop"

---

## Scene 13 — great_hall.jpg
**File:** `static/svg/great_hall.svg` → replace with `great_hall.jpg`
**Used in:** great_hall_entrance, all odrik_* scenes

**Midjourney:**
```
interior of a viking great hall frozen in time, forty warriors sitting at long
wooden tables mid-feast with cups raised and mouths open as if interrupted
mid-conversation, none of them moving, candles burning without melting, food
on the tables that has not spoiled, at the far end of the hall a single older
man in a dark ink-stained robe sits alone at the head table watching, warm
amber candlelight against cold stone walls, deep shadows in the rafters, dark
fantasy, painterly, desaturated, deeply wrong stillness, the wrongness of a
moment held too long --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**
```
viking great hall frozen mid-feast, forty warriors at tables cups raised
mouths open interrupted, food unspoiled candles unmelted, lone older man
in dark robe at head table watching, amber candlelight cold stone, deep
shadows, dark fantasy, painterly, desaturated, uncanny stillness, cinematic
```
