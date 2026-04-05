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
a single ancient bone cairn made of dark stacked stones inside a collapsed viking longhouse, broken wooden 
beams and a partially fallen roof framing the scene, remnants of carved pillars and charred timber surrounding it, 
the cairn perfectly intact at the center, runes carved into the stones glowing faintly amber-gold, warm fire 
burning inside through narrow carved gaps, faint cold starlight filtering through the broken roof above, 
thin mist pooling along the floor, enclosed yet ruined space, the structure feels held rather than fully collapsed, 
unnatural stillness, sacred and intimate atmosphere, dark fantasy, painterly, desaturated, deeply unsettling 
stillness --ar 16:9 --style raw --v 6 --stylize 800
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

## Scene 13 — great_hall.jpg

**File:** `static/svg/great_hall.svg` → replace with `great_hall.jpg`
**Used in:** great_hall_entrance, great_hall_rune_door, most odrik_* scenes

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

---

## Scene 14a — forest.jpg

**File:** `static/svg/forest.png`
**Used in:** forest_path, forest_wolf

**Midjourney:**

```
an ancient dark nordic forest at night, enormous gnarled oak trees so dense
their canopies block all sky, roots erupting from black earth like fingers,
a narrow barely-visible path disappearing between the trunks, thick grey fog
pooling at ground level, pale diffuse light with no visible source, the
suggestion of something large and pale moving between the trees in the middle
distance, oppressive suffocating darkness, dark fantasy, painterly,
desaturated, deeply atmospheric, the forest is old and does not want you here
--ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**

```
ancient nordic forest night, enormous gnarled oak trees dense canopy, roots
like fingers black earth, narrow path disappearing in fog, pale diffuse light,
pale shape moving between trees in distance, oppressive darkness, old forest
hostile atmosphere, dark fantasy, painterly, desaturated, cinematic
```

---

## Scene 14a.2 — combat_dire_wolf.jpg

**File:** `static/svg/combat_dire_wolf.png`
**Used in:** forest_wolf (combat encounter)

**Midjourney:**

```
a massive pale dire wolf in a dark ancient forest, unnaturally large, ash-grey
fur matted with old blood and fog, standing in a gap between enormous oak
roots, facing the viewer with flat pale eyes that show neither fear nor hunger,
just assessment, thick fog at ground level, cold diffuse light from above
catching its breath in the freezing air, the wolf is the biggest living thing
in this forest, dark fantasy, painterly, desaturated, predator stillness,
deeply unsettling --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**

```
massive dire wolf ancient dark forest, unnaturally large ash-grey fur, flat
pale eyes assessing not afraid, standing between enormous oak roots, thick fog
ground level, cold light catching breath in air, biggest creature in forest,
dark fantasy, painterly, desaturated, predator stillness, unsettling
```

---

## Scene Act1 — combat_wolf_battlefield.jpg

**File:** `static/svg/combat_wolf_battlefield.png`
**Used in:** combat_wolf_battlefield (battlefield wolf pack encounter)

**Midjourney:**

```
a massive pale dire wolf in dense battlefield, ash-grey fur matted with old blood,
facing the viewer with flat pale eyes that show neither fear nor hunger, just
assessment, cold diffuse light from above catching its breath in the freezing air,
dark fantasy, painterly, desaturated, predator stillness, deeply unsettling
--ar 16:9 --style raw --v 6 --stylize 800
```

---

## Scene 14b — hermit_oak.jpg

**File:** `static/svg/hermit_oak.png`
**Used in:** hermit_oak, hermit_greet, hermit_battlefield, hermit_who, hermit_why, hermit_silence, hermit_oath, hermit_depart

**Midjourney:**

```
a single enormous ancient oak tree at the center of a dark nordic forest,
trunk wider than three men with arms outstretched, runes carved deep into the
bark half-swallowed by decades of growth, exposed roots creating a natural
alcove at the base, an old man seated cross-legged in the alcove with a
wooden staff across his knees, eyes closed, long white hair, worn traveller's
cloak, utterly still, cold fog around the roots, faint amber glow from the
runes, the tree is the oldest thing in the world, dark fantasy, painterly,
desaturated, sacred and unsettling --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**

```
enormous ancient oak tree dark forest, trunk wider than three men, runes
carved half-swallowed by bark, old man seated cross-legged at base staff
across knees eyes closed white hair traveller cloak, cold fog at roots,
faint amber rune glow, oldest tree in the world, sacred and unsettling,
dark fantasy, painterly, desaturated, cinematic
```

---

## Act III — The Silence Beneath

---

## Scene A1 — tyr_temple.png

**File:** `static/svg/tyr_temple.png`
**Used in:** act_3_intro, tyr_temple_approach, tyr_temple_wait, tyr_farewell

**Midjourney:**

```
a small ancient Norse stave temple deep in dark forest, weathered black
timber with no carvings no runes, listing slightly as if leaning into a
wind that has blown for centuries, warm steady light visible through gaps
in the wood — not fire, something steadier than fire, surrounding fog
stops abruptly at the tree line as if something older than the fog drew
a line and the fog respected it, cold diffuse light outside, overcast
sky pressing low, dark fantasy, painterly, desaturated, deeply sacred
and deeply wrong --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**

```
small ancient Norse stave temple dark forest, weathered black timber no
carvings, listing slightly, steady warm light through gaps not fire,
fog stops at tree line, cold diffuse light outside, overcast sky,
sacred and wrong, dark fantasy, painterly, desaturated, cinematic
```

---

## Scene A2 — tyr.png

**File:** `static/svg/tyr.png`
**Used in:** tyr_temple_interior, tyr_dialogue_no_words, tyr_dialogue_grief, tyr_judgement

**Midjourney:**

```
ancient Norse god sitting on a stone floor with his back against a
rough timber wall, tall one-handed right wrist stump not hidden,
calm world-weary expression not angry not kind just honest,
dim flameless light from a shallow bowl on the ground, low timber
ceiling, no throne no altar just stone and wood and age,
wide cinematic composition, figure occupies left third of frame,
dark fantasy, muted grey amber palette, painterly
--ar 16:9 --style raw --v 6 --stylize 800
```

**Note:** Previous generation came out 1024×1536 (portrait). Must generate
as landscape 16:9. The `--ar 16:9` flag is required.

**Stable Diffusion:**

```
ancient Norse god sitting on stone floor rough timber wall, tall
one-handed right wrist stump not hidden, calm world-weary not angry,
dim flameless light from bowl on ground, low timber ceiling, no throne
just stone and wood, dark fantasy portrait, muted grey amber palette,
painterly, intimate, cinematic
```

---

## Scene A3 — firepit.png

**File:** `static/svg/firepit.png`
**Used in:** act_3_intro

**Midjourney:**

```
a small fire burning alone in open darkness, no structure around it,
just packed earth and the circle of amber light it throws, a single
figure sitting motionless beside it seen from behind — hunched slightly,
one hand resting open on a knee, something small held loosely in the
fingers, the fire the only light source, fog pressing at the edges of
the light but not entering, the feeling of a long journey paused not
ended, wide cinematic composition, dark fantasy, painterly, desaturated
except for the amber of the fire, intimate and still
--ar 16:9 --style raw --v 6 --stylize 800
```

---

## Scene 14 — odrik_go_forward.jpg

**File:** `static/svg/odrik_go_forward.svg` → replace with `odrik_go_forward.jpg`
**Used in:** odrik_go_forward

**Midjourney:**

```
close portrait of an aged viking adviser in a dark ink-stained robe seated
at a great hall head table, an empty cup resting on the table before him,
hands still and open, eyes looking directly at the viewer with the weight
of long-held knowledge, forty frozen warriors blurred in deep background,
amber candlelight catching the lines of his face, the stillness of a man
who has just released something he could not release before, dark fantasy,
painterly, desaturated, intimate, heavy silence --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**

```
aged viking adviser dark ink-stained robe, seated at great hall table,
empty cup before him, hands open still, eyes direct at viewer, weight of
held knowledge, frozen warriors blurred background, amber candlelight,
just released long-held secret, dark fantasy, painterly, desaturated,
intimate portrait, heavy silence, cinematic
```

---

## Scene 22 — crossroads.png

**File:** `static/svg/crossroads.png`
**Used in:** crossroads_memory

**Midjourney:**

```
a fog-filled crossroads at night, four paths vanishing into grey
nothingness, no signs no markers, the paths are ancient packed earth
worn by centuries of feet, a thin cold light from no visible source
illuminates the junction, a figure stands at the centre seen from behind
— small against the fog, one hand slightly raised, something held in the
fingers, the fog does not move, the crossroads feels older than the land
around it, the sense of a place where choices become permanent,
wide cinematic composition, dark fantasy, painterly, desaturated,
vast and intimate at once --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**

```
fog-filled crossroads night, four paths vanishing into grey fog,
no signs or markers, ancient packed earth, cold sourceless light,
figure seen from behind at centre, small against emptiness, one hand
raised holding small object, fog motionless, ancient timeless place,
choices made permanent here, dark fantasy, painterly, desaturated,
vast cinematic, wide composition
```

---

## Scene 23 — odin.png

**File:** `static/svg/odin.png`
**Used in:** odin_appears and Odin encounter scenes

**Midjourney:**

```
an old man standing at a foggy crossroads facing the viewer,
one eye — the left socket empty and dark, a wide-brimmed traveller's
hat casting shadow over gaunt features, a staff in one hand worn smooth
by age, plain travelling clothes, no armour no throne no ravens — just
an old man who has been everywhere and seen everything and is very tired,
fog around him but not touching him, the feeling that he was already there
before you arrived and will be there after you leave, wide cinematic
composition, figure occupies centre-left third of frame, dark fantasy,
painterly, desaturated, quiet menace --ar 16:9 --style raw --v 6 --stylize 800
```

**Stable Diffusion:**

```
old one-eyed man at foggy crossroads, empty left eye socket, wide-brimmed
traveller hat, gaunt weathered face, staff worn smooth, plain travelling
clothes, no armour, exhausted ancient presence, fog around him not touching,
was already there before you arrived, dark fantasy, painterly, desaturated,
quiet menace, cinematic wide composition, centre-left framing
```
