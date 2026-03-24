# ============================================================
#  content/scenes.py
#  All scenes for Act 1 — The Battlefield of Silence.
#  Pure data. No logic. The engine in scene.py runs these.
# ============================================================

# ─────────────────────────────────────────────────────────────
#  AWAKENING
# ─────────────────────────────────────────────────────────────
# ── Name entry: shown first, before any choices ──────────────
SCENE_NAME_ENTRY = {
    "header": {
        "title":    "FORGOTTEN AMONG THE FALLEN",
        "subtitle": "A Viking Dark Fantasy",
    },
    "show_hud": False,
    "beats": [
        {
            "type": "prose",
            "text": (
                "You do not remember dying. "
                "You remember the mud, the screaming, the axe rising above you — "
                "and then nothing. "
                "Now there is only silence, fog, and ten thousand corpses. "
                "And you are standing among them."
            )
        },
        {
            "type": "prose",
            "text": (
                "The sky above is the colour of an old bruise. "
                "No crows. No flies. No sound but the wind moving through the dead. "
                "You look at your hands. They are yours. "
                "You look at the bodies. They are not moving. "
                "Not yet."
            )
        },
        {
            "type": "prose",
            "text": (
                "A name sits at the edge of your memory like a word in a language "
                "you used to speak. You reach for it."
            )
        },
        {
            "type": "input",
            "prompt": "  Your name: ",
            "store_as": "name",
        },
    ],
    "next": "awakening",
}

# ── Awakening: choices shown after name is known ──────────────
SCENE_AWAKENING = {
    "header": {
        "title":    "THE WAKING FIELD",
        "subtitle": "you should not be standing",
    },
    "show_hud": False,
    "beats": [
        {
            "type": "prose",
            "text": (
                "The battlefield stretches in every direction — a field of mud and iron "
                "that has swallowed an entire army whole. "
                "You can see the remnants of shield-walls, the broken lines where men "
                "stood their ground and were ground down. "
                "No side won here. Both sides lost everything."
            )
        },
        {
            "type": "prose",
            "text": (
                "You do not know how long you have been lying among them. "
                "You do not know why you rose when they did not. "
                "You know your name — the fog gave that back to you, at least — "
                "but everything else sits just beyond reach, "
                "like words in a language you are forgetting."
            )
        },
        {
            "type": "italic",
            "text": (
                "Somewhere to the north, the ruins of a longhouse. "
                "To the east, the dead lie thicker — the fighting was hardest there. "
                "To the south, a burial mound rises from the earth like a held breath. "
                "And somewhere nearby, you can hear something. "
                "A voice, or what is left of one."
            )
        },
    ],
    "choices": [
        {
            "label":     "Stand still. Listen. Try to understand where you are.",
            "next":      "battlefield_open",
            "effects":   {"resolve": 5},
            "narration": (
                "You breathe. Slowly. The fog shifts around you. "
                "You are alive — or something close enough to alive that the difference "
                "does not matter yet."
            ),
        },
        {
            "label":     "Move. Find someone. Find anything still breathing.",
            "next":      "battlefield_open",
            "effects":   {"resolve": -3, "brutality": 2},
            "narration": (
                "You start walking before you have decided where. "
                "Somewhere in the fog, something shifts. "
                "It might be the wind."
            ),
        },
        {
            "label":     "Look for a weapon. Whatever happened, you will not face it unarmed.",
            "next":      "find_weapon",
            "effects":   {"brutality": 5},
            "narration": (
                "There are weapons everywhere. The dead have no use for them. "
                "You do."
            ),
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  FIND WEAPON (branch from awakening)
# ─────────────────────────────────────────────────────────────
SCENE_FIND_WEAPON = {
    "show_hud": False,
    "beats": [
        {
            "type": "prose",
            "text": (
                "You pull an axe from the mud. "
                "The handle is cracked, the head rusted to the colour of dried blood. "
                "It is heavier than you remember axes being — "
                "though you cannot yet say what you remember."
            )
        },
        {
            "type": "item",
            "item": "rusted axe",
            "action": "give",
        },
        {
            "type": "prose",
            "text": (
                "You test its balance. Your hands know what to do. "
                "That is something. "
                "Your hands remember even when you do not."
            )
        },
    ],
    "choices": [
        {
            "label":   "Grip it tight. Step forward.",
            "next":    "battlefield_open",
            "effects": {"brutality": 2},
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  BATTLEFIELD — OPEN
# ─────────────────────────────────────────────────────────────
SCENE_BATTLEFIELD_OPEN = {
    "header": {
        "title":    "THE BATTLEFIELD OF SILENCE",
        "subtitle": "The Waking Field",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "The battlefield stretches in every direction. "
                "Shields split like eggshells. Spears driven into the earth at strange angles, "
                "as though the ground swallowed them mid-throw. "
                "You count banners — two factions, neither of which you recognise. "
                "Or perhaps you recognise both, and the memory refuses to surface."
            )
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: s.curse_stacks >= 2,
                    "text": (
                        "The fog is heavier than before. At the edge of your vision, "
                        "shapes move that stop when you look at them. "
                        "You are being watched. You have been watched since you woke."
                    ),
                },
                {
                    "text": (
                        "The fog is thick but still. Whatever you expected a battlefield "
                        "to smell like, it does not smell like that. "
                        "It smells like iron, cold earth, and something you have no word for."
                    ),
                },
            ]
        },
        {
            "type": "prose",
            "text": (
                "To the north, a structure — or what is left of one. "
                "The ribs of a longhouse, collapsed inward. "
                "To the east, the battlefield thickens. "
                "Bodies upon bodies. The fighting was densest there. "
                "Closer, perhaps thirty paces west, a man sits against a shattered shield-wall. "
                "He is not one of the dead. Not yet."
            )
        },
    ],
    "choices": [
        {
            "label":     "Go to the man against the shield-wall.",
            "next":      "soul_leif",
            "condition": lambda s: not s.has_flag("leif_done"),
        },
        {
            "label":     "Search the longhouse ruins to the north.",
            "next":      "longhouse_ruins",
            "effects":   {"resolve": 2},
            "condition": lambda s: not s.has_flag("found_forge"),
        },
        {
            "label":     "Search the forge again.",
            "next":      "forge_search",
            "condition": lambda s: s.has_flag("found_forge") and not s.has_flag("forge_searched"),
        },
        {
            "label":     "Move east into the dense dead. Scavenge.",
            "next":      "scavenge_east",
            "effects":   {"brutality": 3},
            "condition": lambda s: not s.has_flag("east_searched"),
        },
        {
            "label":     "Go south — towards the mound.",
            "next":      "the_mound",
            "condition": lambda s: s.has_flag("found_forge") or s.has_flag("east_searched"),
        },
        {
            "label":     "Look around. There must be more here.",
            "next":      "battlefield_look_around",
            "condition": lambda s: (
                not s.has_flag("found_forge") and
                not s.has_flag("east_searched") and
                s.has_flag("leif_done")
            ),
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  SOUL: LEIF — The Dying Soldier
# ─────────────────────────────────────────────────────────────
SCENE_SOUL_LEIF = {
    "header": {
        "title":    "THE DYING SOLDIER",
        "subtitle": "A bound soul — not yet gone",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "He is not dead. Not quite. "
                "An arrow in his side, driven deep enough that you cannot tell if it is "
                "keeping him alive or simply preventing him from dying quickly. "
                "He watches you approach with eyes that have given up being afraid."
            )
        },
        {
            "type": "italic",
            "text": '"You\'re standing," he says. "How are you standing?"',
        },
        {
            "type": "prose",
            "text": (
                "You look at him. You look at your hands. "
                "You do not have a good answer."
            )
        },
        {
            "type": "italic",
            "text": '"Everyone here is dead," he says. "I watched them fall. I fell. You fell."',
        },
        {"type": "pause"},
        {
            "type": "italic",
            "text": '"Your name is—" He stops. His eyes go strange. "I cannot remember your name. I knew it. An hour ago I knew it."',
        },
    ],
    "choices": [
        {
            "label":     '"Tell me what happened here."',
            "next":      "leif_battle_account",
            "effects":   {"resolve": 3},
        },
        {
            "label":     '"Tell me my name."',
            "next":      "leif_gives_name",
            "effects":   {"resolve": 5},
        },
        {
            "label":     '"Who is still alive?"',
            "next":      "leif_survivors",
            "effects":   {"honour": 3},
        },
        {
            "label":     "He is dying. Stay with him until he is gone.",
            "next":      "leif_mercy_kill",
            "effects":   {"mercy": 8, "honour": 5},
            "narration": (
                "You do not leave. That is all. "
                "Sometimes that is enough."
            ),
        },
    ],
}

SCENE_LEIF_GIVES_NAME = {
    "beats": [
        {
            "type": "italic",
            "text": '"I knew it," he says again, slower. "We all knew it. You were—"',
        },
        {"type": "delay", "seconds": 1.2},
        {
            "type": "prose",
            "text": (
                "He says your name. "
                "It hits you like cold water — not because it is surprising, "
                "but because something in your chest clicks into place when you hear it. "
                "A lock finding its key."
            )
        },
        {
            "type": "memory",
            "key":   "my_name",
            "label": "Your name, spoken by a dying man",
            "text":  (
                "Your name. You had it all along, but you needed someone else "
                "to say it aloud to believe it. "
                "This is the first thing you are certain of since you woke."
            ),
        },
        {"type": "stat", "changes": {"resolve": 8, "honour": 5}},
        {
            "type": "italic",
            "text": '"You were Gunnar\'s man," Leif says. "His second. His most trusted. Until the night you weren\'t."',
        },
        {"type": "pause"},
    ],
    "choices": [
        {
            "label":     '"What did I do?"',
            "next":      "leif_the_oath",
        },
        {
            "label":     '"Who is Gunnar?"',
            "next":      "leif_gunnar_intro",
        },
        {
            "label":     "Do not ask. You are not certain you want to know.",
            "next":      "leif_farewell",
            "effects":   {"resolve": -5},
        },
    ],
}

SCENE_LEIF_THE_OATH = {
    "beats": [
        {
            "type": "italic",
            "text": (
                '"You broke the oath," Leif says. '
                '"The oath of the drengr. '
                'You swore to stand at Gunnar\'s shield. '
                'On the last night, when the Svear came from the eastern ridge — '
                'you were not there."'
            ),
        },
        {"type": "pause"},
        {
            "type": "italic",
            "text": '"He held the line. Forty of them, eight of us, without you. He held it until there was nothing left to hold."',
        },
        {
            "type": "prose",
            "text": (
                "The words drop into you like stones into deep water. "
                "You wait for the guilt. "
                "It arrives slowly — it has had time to age."
            )
        },
        {
            "type": "italic",
            "text": (
                '"I always thought," Leif says quietly, "that there was a reason. '
                'Not cowardice — I knew you four years, and you were not a coward. '
                'A debt, maybe. Something you found out. '
                'Something about Gunnar that you could not live with '
                'and could not say out loud."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"Whatever it was — it was enough for you. '
                'Whether it was enough to justify it... '
                'that is a different question."'
            ),
        },
        {
            "type": "memory",
            "key":   "the_broken_oath",
            "label": "The night of the eastern ridge",
            "text":  (
                "You were not there. You do not yet know why. "
                "But Leif's guess sits in you like an ember — "
                "not because it is right, but because it is close enough to feel warm."
            ),
        },
    ],
    "choices": [
        {
            "label":     '"Where is Gunnar now?"',
            "next":      "leif_gunnar_intro",
        },
        {
            "label":     '"I had a reason."',
            "next":      "leif_defense",
            "effects":   {"honour": -5, "resolve": 5},
        },
        {
            "label":     "Say nothing. There is nothing to say.",
            "next":      "leif_farewell",
            "effects":   {"honour": 5, "resolve": -3},
        },
    ],
}

SCENE_LEIF_GUNNAR_INTRO = {
    "beats": [
        {
            "type": "italic",
            "text": '"Gunnar is here. Somewhere in the dead. He\'s been here since the battle ended."',
        },
        {
            "type": "italic",
            "text": '"He does not sleep like the others sleep. He walks. He has been walking since it ended."',
        },
        {
            "type": "prose",
            "text": (
                "Leif\'s breath is shallow now. Each one is a decision. "
                "He has made his peace with the final one."
            )
        },
        {
            "type": "italic",
            "text": (
                '"Go to the mound. He will be there. '
                'And go to the cairn first — it still burns. '
                'Whatever you owe Gunnar, do not face it on empty ground."'
            ),
        },
    ],
    "choices": [
        {
            "label":     '"Thank you, Leif."',
            "next":      "leif_farewell",
            "effects":   {"honour": 5, "mercy": 3},
        },
        {
            "label":     "Leave without a word. The dead do not need courtesy.",
            "next":      "battlefield_open",
            "effects":   {"honour": -3, "brutality": 2},
            "flags":     {"leif_done": True},
        },
    ],
}

# Fallback scene — shown when player has talked to Leif but not yet
# explored enough to unlock the mound path
SCENE_BATTLEFIELD_LOOK_AROUND = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "You stop and take stock. The fog shifts but does not clear. "
                "You have learned to read this battlefield the way you would read a room — "
                "what is present, what is missing, what has been moved."
            )
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: (
                        s.has_flag("found_forge") and
                        s.has_flag("east_searched") and
                        s.has_flag("leif_done")
                    ),
                    "text": (
                        "The longhouse to the north: searched. The forge inside it, cold but yielded what it had. "
                        "To the east: the dense dead, and whatever woke among them, settled now. "
                        "The soldier against the shield-wall: gone, one way or another. "
                        "To the south the mound waits, and Gunnar with it. "
                        "There is nothing left to find here. Only the reckoning."
                    ),
                },
                {
                    "condition": lambda s: (
                        s.has_flag("found_forge") and
                        s.has_flag("east_searched")
                    ),
                    "text": (
                        "The longhouse to the north: searched, the forge cold but generous. "
                        "To the east: you have walked among the dense dead and returned. "
                        "A soldier still breathes against the shield-wall to the west — "
                        "or did, when you last looked. "
                        "To the south, the mound. You have not gone there yet."
                    ),
                },
                {
                    "condition": lambda s: s.has_flag("found_forge"),
                    "text": (
                        "The longhouse to the north: searched. The forge inside still breathes. "
                        "To the east, the dead lie thickest — you have not gone there yet. "
                        "Something moved among them, earlier. You remember that. "
                        "To the south, the mound."
                    ),
                },
                {
                    "condition": lambda s: s.has_flag("east_searched"),
                    "text": (
                        "The longhouse to the north: you have not searched it. "
                        "There is smoke from somewhere inside — cold smoke, old smoke. "
                        "To the east: done. The dead there are settled, mostly. "
                        "A soldier still lives against the western shield-wall. "
                        "To the south, the mound."
                    ),
                },
                {
                    # Default — nothing explored yet
                    "text": (
                        "To the north: longhouse ruins, partially standing. "
                        "You can see the shape of a forge through the collapsed timbers. "
                        "To the east: the dead lie thickest there — the last stand, by the look of it. "
                        "To the west: a soldier, not quite dead, against a broken shield-wall. "
                        "To the south: a mound. Old and deliberate. "
                        "Someone is standing on it."
                    ),
                },
            ],
        },
    ],
    "choices": [
        {
            "label":     "Search the longhouse ruins to the north.",
            "next":      "longhouse_ruins",
            "effects":   {"resolve": 2},
            "condition": lambda s: not s.has_flag("found_forge"),
        },
        {
            "label":     "Go east — into the dense dead.",
            "next":      "scavenge_east",
            "effects":   {"brutality": 3},
            "condition": lambda s: not s.has_flag("east_searched"),
        },
        {
            "label":     "Go to the soldier against the shield-wall.",
            "next":      "soul_leif",
            "condition": lambda s: not s.has_flag("leif_done"),
        },
        {
            "label":     "Go south — towards the mound.",
            "next":      "the_mound",
            "condition": lambda s: (
                s.has_flag("found_forge") or s.has_flag("east_searched")
            ),
        },
        {
            "label":     "Return to the wider battlefield.",
            "next":      "battlefield_open",
        },
    ],
}

SCENE_LEIF_FAREWELL = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "You move to leave. Leif's hand finds your wrist — "
                "not a grip, just a weight. "
                "He presses something into your palm."
            )
        },
        {
            "type": "italic",
            "text": (
                '"I found this the morning after the battle. '
                'Before the wound got bad enough that I stopped moving. '
                'It was on the mound — just sitting there, like it had been left. '
                'I do not know what it opens. '
                'But I kept it. '
                'I think I kept it for you."'
            ),
        },
        {
            "type": "item",
            "item": "Leif's token",
            "action": "give",
        },
        {
            "type": "prose",
            "text": (
                "You leave him to it. "
                "There is dignity in the way he is dying — "
                "upright, eyes open, no theatrics. "
                "You hope your own death had something like that. "
                "You suspect it did not."
            )
        },
        {"type": "flag", "key": "leif_done"},
    ],
    "next": "battlefield_open",
}

SCENE_LEIF_MERCY_KILL = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "You stay. You do not speak. "
                "There is nothing useful to say and Leif is past needing it. "
                "His breathing slows in the way that breathing slows "
                "when there is no more reason to rush."
            )
        },
        {
            "type": "italic",
            "text": (
                '"Good," he says. Not to you, specifically. '
                'Just: good. Like a man setting down something he has carried a long way.'
            )
        },
        {
            "type": "prose",
            "text": (
                "When it is over you sit with it for a moment. "
                "Then you search him — not out of disrespect, "
                "but because the dead have no use for what they carry "
                "and you are not yet done with this battlefield."
            )
        },
        {
            "type": "prose",
            "text": (
                "He has a knife, a pouch of echo dust, and a piece of birchbark "
                "with a name scratched into it. "
                "The name is yours. "
                "He carried it with him into the battle. "
                "You do not know yet whether that makes the weight lighter or heavier."
            )
        },
        {
            "type": "item",  "item": "Leif's knife",  "action": "give"},
        {"type": "shards", "amount": 45},
        {
            "type": "memory",
            "key":   "leif_last_word",
            "label": "What Leif said at the end",
            "text":  (
                "Good. That was all. "
                "One word, said the way you say a word "
                "when it is the last one and it has to be enough. "
                "It was enough."
            ),
        },
        {"type": "flag", "key": "leif_done"},
    ],
    "next": "battlefield_open",
}

SCENE_LEIF_DEFENSE = {
    "beats": [
        {
            "type": "italic",
            "text": '"Then say it," Leif says. "Say the reason."',
        },
        {
            "type": "prose",
            "text": (
                "You open your mouth. "
                "The reason is there — you can feel its shape. "
                "But the words that would carry it are not. "
                "Not yet. "
                "The memory is still fog."
            )
        },
        {
            "type": "italic",
            "text": '"That\'s what I thought," says Leif. He does not say it unkindly.',
        },
    ],
    "next": "leif_gunnar_intro",
}

SCENE_LEIF_BATTLE_ACCOUNT = {
    "beats": [
        {
            "type": "italic",
            "text": (
                '"It was a rout," Leif says. "Both sides. '
                'The Svear came from the east ridge at dawn. '
                'We had a scout there — should have seen them. '
                'We never found the scout."'
            ),
        },
        {
            "type": "italic",
            "text": '"Everyone died. The Svear too. Whatever they wanted from this valley, they didn\'t live to take it."',
        },
        {"type": "stat", "changes": {"resolve": 3}},
        {
            "type": "prose",
            "text": (
                "You file this away. A rout. Both sides destroyed. "
                "No prisoners, no surrender. "
                "The kind of battle that happens when someone makes a catastrophic decision "
                "and no one survives to account for it."
            )
        },
    ],
    "next": "leif_gives_name",
}

SCENE_LEIF_SURVIVORS = {
    "beats": [
        {
            "type": "italic",
            "text": '"No one," Leif says simply. "Only you. And I won\'t be, soon."',
        },
        {
            "type": "prose",
            "text": (
                "He says it without drama. "
                "You find you appreciate that."
            )
        },
    ],
    "next": "leif_gives_name",
}

# ─────────────────────────────────────────────────────────────
#  LONGHOUSE RUINS
# ─────────────────────────────────────────────────────────────
SCENE_LONGHOUSE_RUINS = {
    "header": {
        "title":    "THE LONGHOUSE RUINS",
        "subtitle": "A structure that stood for three generations",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "The longhouse has fallen in on itself — "
                "the central posts gave first, then the roof, "
                "then whatever shape it held. "
                "A fire burned here recently. "
                "Or perhaps a long time ago. Time moves differently on this field."
            )
        },
        {
            "type": "prose",
            "text": (
                "Under a collapsed beam you find the forge. "
                "The coals are cold, but the tools remain. "
                "Someone built this forge to last. "
                "You recognise the craft in it — not because you remember where you learned, "
                "but because your hands do."
            )
        },
        {
            "type": "flag",
            "key":   "found_forge",
        },
        {
            "type": "prose",
            "text": (
                "And then you see it. "
                "Wedged between two stones near the forge mouth: "
                "a bone cairn, still faintly warm. "
                "Runes carved into the topstone — old ones, pre-Christianisation, "
                "the kind your grandmother would have known. "
                "The fire inside it has not gone out."
            )
        },
        {
            "type": "heal",
            "amount": 100,
        },
        {
            "type": "memory",
            "key":   "the_bone_cairn",
            "label": "The warmth of the first cairn",
            "text":  (
                "You place your hand on the cairn and feel something release "
                "in the base of your spine. "
                "A knot you did not know was there. "
                "Whatever else this place is, the cairn is yours. "
                "You will wake here if you fall again."
            ),
        },
    ],
    "choices": [
        {
            "label":     "Rest at the cairn. You have time.",
            "next":      "cairn_rest",
            "effects":   {"resolve": 8},
            "flags":     {"rested_at_cairn": True},
        },
        {
            "label":     "Search the forge for usable materials.",
            "next":      "forge_search",
        },
        {
            "label":     "Return to the battlefield.",
            "next":      "battlefield_open",
        },
    ],
}

SCENE_CAIRN_REST = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "You sit with your back against the cairn. "
                "The warmth is steady — not warm like fire, "
                "but warm like something that has been burning so long "
                "it has forgotten how to stop. "
                "You close your eyes and let the memory try to find you."
            )
        },
        {
            "type": "memory",
            "key":   "the_feast",
            "label": "A feast in the longhouse — before",
            "text":  (
                "The hall is loud. Smoke and mead and a dozen arguments at once. "
                "Someone is singing badly and everyone is letting them. "
                "You are sitting at Gunnar's right hand — "
                "the place of honour, the place of trust — "
                "and he is saying something to you that you cannot quite hear "
                "over the noise. But he is smiling. "
                "You cannot remember the last time you saw him smile. "
                "You cannot remember if he smiled after."
            ),
        },
        {
            "type": "italic",
            "text": (
                "The fire. The faces you know. "
                "Your hand around a cup that is full. "
                "The specific weight of a night when nothing is wrong yet."
            )
        },
        {
            "type": "prose",
            "text": (
                "You open your eyes. "
                "The fog is the same. The battlefield is the same. "
                "But something has shifted — "
                "not in the world, but in the distance between you and what you lost. "
                "It is smaller than it was."
            )
        },
        {"type": "heal", "amount": 30},
    ],
    "next": "battlefield_open",
}

SCENE_FORGE_SEARCH = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "The forge is cold but not abandoned. "
                "Someone was working here right up to the end — "
                "a blade still clamped in the vice, "
                "half its edge reground. "
                "The tools are laid out in the order of someone who expected to return. "
                "They did not return."
            )
        },
        {
            "type": "prose",
            "text": (
                "You work through it methodically. "
                "Iron scraps. A whetstone, good quality. "
                "A pouch of echo dust tucked under the bellows — "
                "someone hid it there, which means someone knew what it was worth. "
                "Your hands move through the search with the ease of practice. "
                "You have done this before. After battles, after raids. "
                "The memory does not surface, but the competence does."
            )
        },
        {"type": "item",   "item": "iron scraps", "action": "give"},
        {"type": "item",   "item": "whetstone",   "action": "give"},
        {"type": "shards", "amount": 80},
        {
            "type": "prose",
            "text": (
                "Beneath the workbench, wrapped in oiled cloth: a medallion. "
                "Clan mark. You turn it over in your fingers. "
                "The mark is one you know — not from this battle, "
                "not from any single memory, "
                "but from the deep place where the certain things live. "
                "You have worn this. Or one exactly like it. "
                "The difference, if there is one, does not matter."
            )
        },
        {
            "type": "memory",
            "key":   "the_medallion",
            "label": "A clan medallion, familiar and nameless",
            "text":  (
                "The weight of it is the weight of belonging somewhere. "
                "Of being someone's man. "
                "You wore this mark when you swore the oath. "
                "You do not know if you are still wearing it — "
                "whether the oath broken means the mark void, "
                "or whether the mark outlasts the man who broke it."
            ),
        },
        {"type": "item", "item": "clan medallion", "action": "give"},
        {"type": "flag", "key": "forge_searched"},
    ],
    "next": "battlefield_open",
}

# ─────────────────────────────────────────────────────────────
#  SCAVENGE EAST
# ─────────────────────────────────────────────────────────────
SCENE_SCAVENGE_EAST = {
    "header": {
        "title":    "THE DENSE DEAD",
        "subtitle": "The fighting was hardest here",
    },
    "beats": [
        {"type": "flag", "key": "east_searched"},
        {
            "type": "prose",
            "text": (
                "The eastern section of the battlefield is where it ended. "
                "You can read the story in the bodies: "
                "the last stand, the final push, "
                "the moment when both sides simply ran out of men to send forward. "
                "The dead here lie in pairs, "
                "as though they agreed on some private arrangement."
            )
        },
        {
            "type": "prose",
            "text": (
                "You move through them carefully. Searching. "
                "You tell yourself you are looking for supplies. "
                "This is partly true."
            )
        },
        {"type": "shards", "amount": 120},
        {"type": "item",   "item": "iron scraps",  "action": "give"},
        {
            "type": "prose",
            "text": (
                "Then one of them moves. "
                "Not all at once — a hand first, then a shoulder, "
                "then the slow terrible process of something that has been dead "
                "deciding that it has unfinished business."
            )
        },
        {"type": "pause", "msg": "  [ you are not alone ]"},
    ],
    "choices": [
        {
            "label":     "Stand your ground. Face it.",
            "next":      "combat_draugar_east",
            "effects":   {"honour": 5, "brutality": 3},
        },
        {
            "label":     "Back away slowly. You choose your battles.",
            "next":      "battlefield_open",
            "effects":   {"honour": -3, "resolve": 3},
            "narration": (
                "You back into the fog. "
                "The thing follows you with its eyes — "
                "but eyes are the only thing it can move quickly. "
                "You are gone before the rest of it is upright."
            ),
        },
        {
            "label":     "Strike first. Before it is fully awake.",
            "next":      "combat_draugar_east",
            "effects":   {"brutality": 8, "honour": -5},
            "narration": "You do not give it the chance to stand.",
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  COMBAT SCENES
# ─────────────────────────────────────────────────────────────
SCENE_COMBAT_DRAUGAR_EAST = {
    "beats": [
        {
            "type":  "combat",
            "enemy": "draugar_weak",
            "flag":  "defeated_draugar_east",
        },
        {"type": "stat", "changes": {"brutality": 3}},
    ],
    "choices": [
        {
            "label":     "Search the bodies more carefully.",
            "next":      "scavenge_east_after",
        },
        {
            "label":     "Return to the wider battlefield.",
            "next":      "battlefield_open",
        },
    ],
}

SCENE_SCAVENGE_EAST_AFTER = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "The battlefield settles again. "
                "You stand in it, breathing. "
                "The quiet after violence is a specific kind of quiet. "
                "You recognise it."
            )
        },
        {
            "type": "prose",
            "text": (
                "Now that the immediate threat is settled, you search properly. "
                "The dead here carry more than the others — "
                "this was where the officers fell."
            )
        },
        {"type": "shards", "amount": 180},
        {"type": "item",   "item": "reinforced vambrace", "action": "give"},
        {
            "type": "memory",
            "key":   "the_officers",
            "label": "The rank of those who fell last",
            "text":  (
                "Officers. Senior men. "
                "You recognise the clan marks on two of them. "
                "One of them — the largest, face-down in the mud — "
                "wears a commander's torc around his neck. "
                "You do not touch it. "
                "Not yet."
            ),
        },
    ],
    "next": "battlefield_open",
}

# ─────────────────────────────────────────────────────────────
#  THE MOUND — Boss Approach
# ─────────────────────────────────────────────────────────────
SCENE_THE_MOUND = {
    "header": {
        "title":    "THE MOUND OF OATHBREAKERS",
        "subtitle": "Those buried without honour sleep lightly here",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "The mound rises at the battlefield's southern edge — "
                "a mass burial, older than this battle. "
                "Oathbreakers, your memory supplies without prompting. "
                "Warriors buried face-down so they could not find their way to Valhalla. "
                "The ground over them is darker than the surrounding earth. "
                "It has been disturbed."
            )
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: s.has_memory("the_broken_oath"),
                    "text": (
                        "You stand at the edge of it for a long time. "
                        "You think about oaths. "
                        "You think about the shape of the one you broke — "
                        "still foggy, still incomplete, "
                        "but present in the way that a word on the tip of your tongue is present. "
                        "You can almost say it."
                    ),
                },
                {
                    "text": (
                        "There is a figure at the mound's crown. "
                        "Standing still. "
                        "You have been aware of it since you entered this part of the field, "
                        "the way you are aware of something very cold nearby."
                    ),
                },
            ]
        },
        {
            "type": "prose",
            "text": (
                "He is waiting for you. "
                "He has been waiting for you since before you woke."
            )
        },
        {
            "type": "italic",
            "text": '"I knew you would come here," says Gunnar. "This is where oathbreakers end up."',
        },
        {"type": "pause"},
        {
            "type": "prose",
            "text": (
                "He looks like you remember — "
                "though you are still assembling what you remember. "
                "Tall. A stillness to him that was authority when he was alive "
                "and is something else now. "
                "His eyes have the blue-grey light of the deep dead. "
                "But he is speaking. "
                "The deep dead do not speak."
            )
        },
    ],
    "choices": [
        {
            "label":     '"I am not here to fight you."',
            "next":      "gunnar_dialogue_peace",
            "effects":   {"honour": 5},
        },
        {
            "label":     '"Then this is where I end it."',
            "next":      "gunnar_dialogue_challenge",
            "effects":   {"brutality": 5, "resolve": 5},
        },
        {
            "label":     '"Tell me what I did."',
            "next":      "gunnar_dialogue_truth",
            "condition": lambda s: s.has_memory("the_broken_oath"),
        },
    ],
}

SCENE_GUNNAR_DIALOGUE_PEACE = {
    "beats": [
        {
            "type": "italic",
            "text": '"That is not your decision," Gunnar says. "It was not mine, either."',
        },
        {
            "type": "italic",
            "text": '"You broke the oath. The field will not release you until you face what that means. Neither will I."',
        },
        {
            "type": "prose",
            "text": "He raises his axe. The movement is tired. He has done it many times before.",
        },
    ],
    "next": "combat_gunnar",
}

SCENE_GUNNAR_DIALOGUE_CHALLENGE = {
    "beats": [
        {
            "type": "italic",
            "text": '"Good," says Gunnar. "At least be honest about it."',
        },
        {
            "type": "prose",
            "text": (
                "He looks at you for a long moment. Not with hatred — you expected "
                "hatred and would have understood it. "
                "What you see is something closer to relief."
            )
        },
        {
            "type": "italic",
            "text": (
                '"I have been standing on this mound for six days," he says. '
                '"Waiting for you to come. '
                'I knew you would come eventually. You always came back, in the end."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "He rolls his shoulders. The axe comes up. "
                "The movement is not angry — it is practiced. "
                "He has done this ten thousand times. "
                "He taught you to do this."
            )
        },
        {"type": "stat", "changes": {"resolve": 5}},
    ],
    "next": "combat_gunnar",
}

SCENE_GUNNAR_DIALOGUE_TRUTH = {
    "beats": [
        {
            "type": "italic",
            "text": '"You know what you did," Gunnar says. "The fog does not help you here. I was there."',
        },
        {
            "type": "italic",
            "text": '"You left your position. You left us. In forty years of war, I trusted three men with my life. You were the last."',
        },
        {"type": "pause"},
        {
            "type": "memory",
            "key":   "the_truth",
            "label": "What Gunnar remembers",
            "text":  (
                "He is telling the truth. "
                "You can feel it — not the words, but the truth underneath them. "
                "You left. You had a reason. "
                "The reason is very close now. "
                "You can almost touch it."
            ),
        },
        {
            "type": "italic",
            "text": '"Fight me. Or don\'t. Either way, we are not finished."',
        },
    ],
    "next": "combat_gunnar",
}

SCENE_COMBAT_GUNNAR = {
    "beats": [
        {
            "type":  "combat",
            "enemy": "gunnar",
            "flag":  "gunnar_defeated",
        },
    ],
    "choices": [
        {
            "label": "Go to him. Hear what he has to say.",
            "next":  "act1_end",
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  ZONE 1 END
# ─────────────────────────────────────────────────────────────
SCENE_ACT1_END = {
    "header": {
        "title":    "SILENCE FALLS",
        "subtitle": "The Battlefield of Silence — cleared",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "He is on one knee. Not defeated — you do not think he can be defeated, "
                "not truly — but spent. The axe is in the mud. "
                "His hands are open."
            )
        },
        {
            "type": "prose",
            "text": (
                "You look at the axe. It is not a trophy. "
                "You do not pick it up as a trophy. "
                "But you pick it up."
            )
        },
        {
            "type": "item",
            "item": "Gunnar's Axe",
            "action": "give",
        },
        {
            "type": "italic",
            "text": (
                '"I did not wake by choice either," he says. '
                '"I have been here since the last arrow. '
                'I watched every one of them stop moving. '
                'I did not stop."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"I think I am here because of you. '
                'I think I was waiting. '
                'I do not know what I am now that the waiting is done."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "He reaches into his coat and holds something out. "
                "An iron key, old and heavy, marked with a rune you almost recognise."
            )
        },
        {
            "type": "italic",
            "text": (
                '"Take it. It opens something to the south — '
                'I found it on the third day, when I was still looking for a reason. '
                'I think the reason is you."'
            ),
        },
        {
            "type": "item",
            "item": "Remembrance Key",
            "action": "give",
        },
        {
            "type": "memory",
            "key":   "the_first_victory",
            "label": "What it felt like to defeat your commander",
            "text":  (
                "It did not feel like victory. "
                "It felt like a door opening into a room "
                "you are not certain you wanted to enter. "
                "You enter anyway. "
                "That is, apparently, what you do."
            ),
        },
        {
            "type": "prose",
            "text": (
                "When you look up, Gunnar is still. "
                "Not gone — you do not think he can be gone — "
                "but still, in the way that a long argument is still "
                "when both sides have said everything true. "
                "For now, that is enough."
            )
        },
        {
            "type": "prose",
            "text": (
                "To the south, the fog is thinner. "
                "Through it you can see the shape of mountains — "
                "or what your memory insists are mountains, "
                "though they have no peaks and do not end. "
                "The key is cold in your hand. "
                "Whatever it opens is through there."
            )
        },
    ],
    "choices": [
        {
            "label":     "Walk south. Into whatever comes next.",
            "next":      "act_2_intro",
            "effects":   {"resolve": 10},
        },
        {
            "label":     "Rest first. The cairn. One more night.",
            "next":      "final_rest",
            "effects":   {"resolve": 5, "honour": 5},
        },
    ],
}

SCENE_FINAL_REST = {
    "header": {
        "title":    "THE BONE CAIRN",
        "subtitle": "one more night",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "You go back to the cairn. "
                "The warmth is still there — it does not seem to diminish, "
                "no matter how long it burns. "
                "You put your back against it and look at the battlefield. "
                "From here it is just shapes in fog. "
                "You can almost believe it is something else."
            )
        },
        {
            "type": "prose",
            "text": (
                "You close your eyes. "
                "The memory comes closer — not all the way, but closer. "
                "You can see the eastern ridge. "
                "You can see the moment. "
                "You can feel the weight of the decision you made, "
                "which is different from understanding it. "
                "You are not yet ready to say it out loud. "
                "But you are closer than you were."
            )
        },
        {
            "type": "italic",
            "text": (
                "The cairn hums very quietly. "
                "Or perhaps that is you. "
                "The distinction has become less important."
            )
        },
        {
            "type": "prose",
            "text": (
                "When you open your eyes the fog to the south is lighter. "
                "Not gone — never gone — but thinner. "
                "The key is warm in your hand. "
                "It is time."
            )
        },
        {"type": "stat", "changes": {"resolve": 8, "honour": 5}},
        {"type": "heal", "amount": 100},
    ],
    "next": "act_2_intro",
}

SCENE_ACT_2_INTRO = {
    "header": {
        "title":    "ACT II",
        "subtitle": "The Truth in the Fog",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "The fog to the south is colder. That is the only difference, at first. "
                "The same grey light. The same silence. "
                "But the cold has a direction to it — "
                "it comes from somewhere specific, "
                "the way cold always comes from somewhere specific "
                "even when you cannot name it."
            )
        },
        {
            "type": "prose",
            "text": (
                "You walk for what might be an hour or might be a day. "
                "You do not tire the way you used to tire. "
                "Your body remembers exhaustion as a concept "
                "but has stopped practising it. "
                "This should be more disturbing than it is."
            )
        },
        {
            "type": "italic",
            "text": (
                "Somewhere behind you, the battlefield. "
                "Ten thousand dead who stayed dead. "
                "One who didn't. "
                "You."
            )
        },
        {
            "type": "prose",
            "text": (
                "The key is in your hand. "
                "It has been warm since Gunnar gave it to you — "
                "not body-warm, but warm the way old iron is warm "
                "when it has been near fire for a long time. "
                "It is pointing you somewhere. "
                "You are beginning to understand that you do not have a choice "
                "about whether to follow."
            )
        },
        {
            "type": "italic",
            "text": "The fog does not lift. It never lifts. But you are still walking in it.",
        },
    ],
    "choices": [
        {
            "label":     "Continue south. The key grows warmer.",
            "next":      "fog_road",
        },
        {
            "label":     "Return to the battlefield (restart Act 1).",
            "next":      "__restart__",
        },
    ],
}

# ═════════════════════════════════════════════════════════════
#  ACT II — THE STIRRING BENEATH
# ═════════════════════════════════════════════════════════════

SCENE_FOG_ROAD = {
    "header": {
        "title":    "THE ROAD SOUTH",
        "subtitle": "the fog does not thin",
    },
    "beats": [
        {
            "type": "prose",
            "text": "The fog south of the battlefield moves differently.",
        },
        {
            "type": "prose",
            "text": "Not wind. There is no wind here. It moves the way breath moves — "
                    "in and out, slow and without intention. You have been walking for "
                    "what feels like an hour. The key is warm against your palm. Not hot. "
                    "Warm. Like something recently held by someone else.",
        },
        {
            "type": "prose",
            "text": "The ground beneath you is not a road. It was a road once — you can "
                    "feel the stones beneath the mud, placed by someone with purpose. "
                    "Now it leads south into nothing you can see.",
        },
        {
            "type": "italic",
            "text": "You hear something ahead. Not a voice. The shape a voice leaves "
                    "after it stops.",
        },
    ],
    "choices": [
        {
            "label": "Stop and listen.",
            "effects": {"honour": 2},
            "next":  "fog_the_held",
        },
        {
            "label": "Keep moving.",
            "next":  "fog_the_held",
        },
        {
            "label": "Look at the key.",
            "next":  "fog_the_held",
        },
    ],
}

SCENE_FOG_THE_HELD = {
    "header": {
        "title":    "THE HELD",
        "subtitle": "they have been standing like this for a long time",
    },
    "beats": [
        {
            "type": "prose",
            "text": "There are two of them.",
        },
        {
            "type": "prose",
            "text": "Not soldiers. A man and a woman, dressed in travelling clothes — "
                    "the kind worn by people who move between settlements, not fight in "
                    "them. They stand in the middle of the road facing each other as if "
                    "mid-conversation. Their feet have sunk slightly into the mud.",
        },
        {
            "type": "prose",
            "text": "They are not dead. Their eyes are open. Their chests rise and fall.",
        },
        {
            "type": "prose",
            "text": "When you step closer, the woman's head turns toward you. Not fast. "
                    "Not threatening. The way a person turns when they hear their name "
                    "spoken in another room.",
        },
        {
            "type": "italic",
            "text": "Her mouth opens. \"Don't,\" she says. Not to you. To the man beside "
                    "her. He doesn't move.",
        },
        {
            "type": "prose",
            "text": "She reaches out and takes your arm. Her grip is cold and absolute.",
        },
        {
            "type": "italic",
            "text": "She is not trying to hurt you. She is trying to hold on.",
        },
    ],
    "choices": [
        {
            "label": "Pull free. Force your way past.",
            "next":  "fog_held_after",
        },
        {
            "label": "Stay still. \"I see you. You can let go.\"",
            "next":  "fog_held_release",
        },
        {
            "label": "Look at the man. The other one hasn't moved.",
            "next":  "fog_held_other",
        },
    ],
}

SCENE_FOG_HELD_OTHER = {
    "beats": [
        {
            "type": "prose",
            "text": "The man has not moved since you arrived. Not his head, not his "
                    "hands. His eyes are fixed on a point somewhere past your left "
                    "shoulder — something that was there before you were, something "
                    "that will still be there after.",
        },
        {
            "type": "italic",
            "text": "He is not unreachable. He is simply very far away.",
        },
        {
            "type": "prose",
            "text": "The woman's grip on your arm tightens. She is watching you watch him.",
        },
    ],
    "choices": [
        {
            "label": "Pull free. You cannot help them.",
            "next":  "fog_held_after",
        },
        {
            "label": "Speak to her. \"You can let go. Both of you.\"",
            "next":  "fog_held_release",
        },
    ],
}

SCENE_FOG_HELD_RELEASE = {
    "beats": [
        {
            "type": "prose",
            "text": "Her grip loosens. Not all at once — finger by finger, the way "
                    "ice thaws.",
        },
        {
            "type": "prose",
            "text": "She doesn't look at you when she releases. She looks at the man "
                    "beside her. Something passes between them that you cannot read. "
                    "He turns his head — slowly, the same way she did — and looks at you.",
        },
        {
            "type": "italic",
            "text": "\"How long,\" he says. Not a question. A statement he has said "
                    "many times before.",
        },
        {
            "type": "prose",
            "text": "You don't know the answer. But you stay until they both face "
                    "forward again — facing south, facing the same direction as you. "
                    "Facing whatever is ahead.",
        },
        {
            "type": "italic",
            "text": "They don't follow. But they stand easier now.",
        },
        {
            "type": "memory",
            "key":   "held_released",
            "label": "What it costs to be seen",
            "text":  "The woman's grip releasing. Finger by finger. The man finally "
                     "turning his head. How long it took. How little it required.",
        },
        {
            "type": "stat",
            "changes": {"honour": 5},
        },
    ],
    "next": "fog_sentinel",
}

SCENE_FOG_HELD_AFTER = {
    "beats": [
        {
            "type": "prose",
            "text": "You are free. The cold of her grip stays on your arm like a "
                    "bruise that hasn't surfaced yet.",
        },
        {
            "type": "prose",
            "text": "She didn't fall. She is still standing. Still reaching toward "
                    "where you were.",
        },
        {
            "type": "italic",
            "text": "You don't look back.",
        },
        {
            "type": "memory",
            "key":   "held_forced",
            "label": "The strength required to leave someone behind",
            "text":  "The cold of her grip. How long it stayed. What it meant that "
                     "leaving was possible at all.",
        },
        {
            "type": "stat",
            "changes": {"brutality": 5},
        },
        {
            "type": "stat",
            "changes": {"health": -15},
        },
        {
            "type": "flag",
            "key":   "held_forced",
            "value": True,
        },
    ],
    "next": "fog_sentinel",
}

SCENE_FOG_SENTINEL = {
    "header": {
        "title":    "THE FOG-SENTINEL",
        "subtitle": "the bell-tone has no source you can name",
    },
    "beats": [
        {
            "type": "prose",
            "text": "You hear it before you see it.",
        },
        {
            "type": "prose",
            "text": "A sound like a bell that was struck once, a long time ago, and "
                    "never finished ringing. Low. Persistent. Coming from everywhere "
                    "and nowhere in the fog ahead.",
        },
        {
            "type": "prose",
            "text": "Then you see the shape. It is tall. Taller than a man, but the "
                    "proportions are wrong — too narrow, too still, arms that hang too "
                    "low. It stands in the centre of the road. It does not breathe. "
                    "It does not move.",
        },
        {
            "type": "prose",
            "text": "But the sound is coming from it.",
        },
        {
            "type": "prose",
            "text": "When you take a step forward, it turns. No neck movement — the "
                    "whole body rotates as one, like a post driven into the ground. "
                    "Its face, if it has one, is hidden in fog. Its hands — too long, "
                    "too thin — rise slowly to its sides.",
        },
        {
            "type": "italic",
            "text": "It is not trapped here. It is keeping something trapped.",
        },
    ],
    "choices": [
        {
            "label": "Attack. Commit fully.",
            "next":  "combat_fog_sentinel",
        },
        {
            "label": "Circle wide. Leave the road entirely.",
            "next":  "fog_sentinel_avoided",
        },
        {
            "label": "Stand still. Wait.",
            "next":  "fog_sentinel_wait",
        },
    ],
}

SCENE_FOG_SENTINEL_WAIT = {
    "beats": [
        {
            "type": "prose",
            "text": "You stop. The bell-tone continues, unchanged.",
        },
        {
            "type": "prose",
            "text": "Then the Sentinel takes one step forward. Slow. Deliberate. "
                    "The fog around it moves with it, as if it is carrying the fog "
                    "rather than walking through it.",
        },
        {
            "type": "italic",
            "text": "Waiting is not an option. It will reach you.",
        },
    ],
    "choices": [
        {
            "label": "Attack now.",
            "next":  "combat_fog_sentinel",
        },
        {
            "label": "Circle wide. Get off the road.",
            "next":  "fog_sentinel_avoided",
        },
    ],
}

SCENE_FOG_SENTINEL_AVOIDED = {
    "beats": [
        {
            "type": "prose",
            "text": "You leave the road. The ground off the path is softer — mud, "
                    "grass, something that might have been a field once. You circle "
                    "wide, keeping the Sentinel in your peripheral vision.",
        },
        {
            "type": "italic",
            "text": "It tracks you the entire time. The whole body rotating, slowly, "
                    "following your arc through the fog. When you reach the road again "
                    "it has not moved from its position. But the sound is gone.",
        },
        {
            "type": "prose",
            "text": "The silence where the bell-tone was feels larger than the sound did.",
        },
        {
            "type": "flag",
            "key":   "sentinel_avoided",
            "value": True,
        },
    ],
    "next": "fog_sentinel_after",
}

SCENE_COMBAT_FOG_SENTINEL = {
    "header": {
        "title":    "THE FOG-SENTINEL",
        "subtitle": "the harder you hit, the more it drinks",
    },
    "beats": [
        {
            "type": "combat",
            "enemy": "fog_sentinel",
        },
    ],
}

SCENE_FOG_SENTINEL_AFTER = {
    "beats": [
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: s.flags.get("sentinel_avoided"),
                    "text": "The road ahead is quieter. Not less thick — quieter. "
                            "As if something that was listening has stopped.",
                },
                {
                    "condition": None,
                    "text": "It falls without a sound. The bell-tone stops mid-ring, "
                            "cut like a thread. The fog where it stood is colder than "
                            "the rest.",
                },
            ],
        },
        {
            "type": "prose",
            "text": "The key pulls south. Ahead, just visible through the fog, is a "
                    "shape that is not fog. Stone. A wall. A gate.",
        },
        {
            "type": "italic",
            "text": "The Stirring Beneath begins.",
        },
    ],
    "next": "gatehouse_approach",
}

SCENE_GATEHOUSE_APPROACH = {
    "header": {
        "title":    "THE GATEHOUSE",
        "subtitle": "someone lit that torch recently",
    },
    "beats": [
        {
            "type": "prose",
            "text": "The wall appears before the gate does.",
        },
        {
            "type": "prose",
            "text": "Stone. Old, but not ancient — built by people who expected it "
                    "to last a generation, not forever. The fog thins slightly here, "
                    "as if the structure itself pushes it back. You can see the top "
                    "of the gatehouse tower. A torch burns there.",
        },
        {
            "type": "italic",
            "text": "Someone lit that torch. Recently.",
        },
        {
            "type": "prose",
            "text": "The gate is open. Not ajar — fully open, both doors pressed back "
                    "against the walls as if welcoming. As if they were opened for "
                    "someone expected.",
        },
        {
            "type": "prose",
            "text": "Two guards stand at the gate. Full armour, spears at rest. Their "
                    "posture is correct — weight balanced, eyes forward, the stance of "
                    "men who take their post seriously. They are not breathing.",
        },
        # Conditional — held_forced changes what happens next
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: s.flags.get("held_forced"),
                    "text": "When you step closer, both of them move. "
                            "Not the slow head-turn of the others — "
                            "this is faster. More deliberate. "
                            "Their spears drop from rest to level in one motion. "
                            "Their eyes find you.",
                },
                {
                    "condition": None,
                    "text": "You watch for a long time. Their chests do not rise. "
                            "Their eyes do not move. But they are standing, "
                            "and their spears are held with purpose, "
                            "and something about them is waiting.",
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: s.flags.get("held_forced"),
                    "text": "They remember. Or something in them does. "
                            "Something passed through the fog before you did — "
                            "something that felt like what you left behind on the road.",
                },
                {
                    "condition": None,
                    "text": "When you step through the gate one of them turns his head. "
                            "Not toward you. Away from you. As if he heard something "
                            "behind him that you cannot hear.",
                },
            ],
        },
    ],
    "choices": [
        {
            "label": "Approach carefully. Hands visible.",
            "next":  "gatehouse_guards_hostile",
            "condition": lambda s: s.flags.get("held_forced"),
        },
        {
            "label": "Step back. Give them space.",
            "next":  "gatehouse_guards_hostile",
            "condition": lambda s: s.flags.get("held_forced"),
        },
        {
            "label": "Look at the guards closely.",
            "next":  "gatehouse_guards",
            "condition": lambda s: not s.flags.get("held_forced"),
        },
        {
            "label": "Look at the courtyard ahead.",
            "next":  "gatehouse_courtyard",
            "condition": lambda s: not s.flags.get("held_forced"),
        },
        {
            "label": "Touch the wall.",
            "next":  "gatehouse_wall",
            "condition": lambda s: not s.flags.get("held_forced"),
        },
    ],
}

SCENE_GATEHOUSE_GUARDS_HOSTILE = {
    "header": {
        "title":    "THE GATEHOUSE",
        "subtitle": "the spears do not lower",
    },
    "beats": [
        {
            "type": "prose",
            "text": "The spears do not lower. "
                    "Their eyes track you — not the vacant gaze of the others "
                    "frozen around the battlefield. "
                    "These are watching. Measuring.",
        },
        {
            "type": "prose",
            "text": "They do not speak. "
                    "They have not spoken in a long time — "
                    "you can see it in the way their mouths are set, "
                    "the silence that has become permanent. "
                    "But they hear. Something in them hears.",
        },
        {
            "type": "italic",
            "text": "Whatever came through the fog before you, "
                    "they felt it. "
                    "It left a mark they recognise.",
        },
    ],
    "choices": [
        {
            "label": "Say nothing. Stand still. Let them look.",
            "next":  "gatehouse_guards_calmed",
            "effects": {"honour": 3},
        },
        {
            "label": "\"I am not here to fight. I came through the fog alone.\"",
            "next":  "gatehouse_guards_spoken",
        },
        {
            "label": "Show them Gunnar's Axe. Let them see whose it is.",
            "next":  "gatehouse_guards_axe",
            "condition": lambda s: s.flags.get("held_forced") and s.equipped_weapon == "Gunnar's Axe",
        },
        {
            "label": "Force your way through.",
            "next":  "gatehouse_guards_forced",
            "effects": {"honour": -5, "brutality": 5},
        },
    ],
}

SCENE_GATEHOUSE_GUARDS_CALMED = {
    "beats": [
        {
            "type": "prose",
            "text": "You stop. You do not reach for anything. "
                    "You let the silence do what words cannot.",
        },
        {
            "type": "prose",
            "text": "The guard on the left — the one who moved first — "
                    "holds longest. The spear point wavers. "
                    "Then, slowly, it drops. Not all the way. "
                    "But enough.",
        },
        {
            "type": "italic",
            "text": "The one on the right follows. "
                    "A beat later, as if checking that the first one meant it.",
        },
        {
            "type": "prose",
            "text": "They do not step aside. "
                    "But there is a gap between them now that was not there before. "
                    "An offering, not a welcome.",
        },
        {
            "type": "memory",
            "key":   "guards_calmed",
            "label": "What stillness can do that force cannot",
            "text":  "The spear lowering. Not because you overpowered them — "
                     "because you gave them time to remember "
                     "that you were not the thing they feared.",
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_GUARDS_SPOKEN = {
    "beats": [
        {
            "type": "prose",
            "text": "Your voice is strange in this place. "
                    "You have not spoken aloud since the battlefield — "
                    "you did not realise until the words came out "
                    "how quiet everything has been.",
        },
        {
            "type": "prose",
            "text": "The guards react to the sound. "
                    "Not to the meaning — to the fact of it. "
                    "Someone is speaking. Someone still can.",
        },
        {
            "type": "italic",
            "text": "The left guard's spear wavers. "
                    "His head tilts — the first unscripted movement "
                    "you have seen from either of them.",
        },
        {
            "type": "prose",
            "text": "It is not understanding. But it is something. "
                    "A crack in whatever holds them here like this.",
        },
        {
            "type": "prose",
            "text": "You keep talking. It does not matter what you say. "
                    "The sound is enough. "
                    "Eventually, the spears come down.",
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_GUARDS_AXE = {
    "beats": [
        {
            "type": "prose",
            "text": "You draw the axe slowly — "
                    "not as a threat, handle first, "
                    "the blade turned away. "
                    "You hold it out so they can see the mark on the head.",
        },
        {
            "type": "italic",
            "text": "Both of them freeze.",
        },
        {
            "type": "prose",
            "text": "They know it. "
                    "Of course they know it — "
                    "they carried spears under the man who carried this. "
                    "They watched him hold it the way you are holding it now.",
        },
        {
            "type": "prose",
            "text": "The spears lower together this time. No hesitation. "
                    "Whatever they are, whatever holds them here, "
                    "there is still something in them that remembers "
                    "what it meant to be sworn to a commander.",
        },
        {
            "type": "italic",
            "text": "They step aside. "
                    "Not because you forced them. "
                    "Because Gunnar's axe asked them to.",
        },
        {
            "type": "memory",
            "key":   "guards_axe_recognition",
            "label": "What the axe still means to those who served under it",
            "text":  "The guards stepping aside for the axe. "
                     "Not for you — for what you carried. "
                     "What that says about Gunnar. "
                     "What it says about you that you have it.",
        },
        {
            "type": "stat",
            "changes": {"honour": 5},
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_GUARDS_FORCED = {
    "beats": [
        {
            "type": "prose",
            "text": "You go through them. "
                    "Not a fight — they are not fast enough for a fight. "
                    "More like moving through a door that resists.",
        },
        {
            "type": "prose",
            "text": "One spear catches your arm. "
                    "The other grazes your shoulder. "
                    "You are through before either of them can bring weight to bear.",
        },
        {
            "type": "italic",
            "text": "Behind you, they do not pursue. "
                    "They return to their positions. "
                    "As if it did not happen. "
                    "As if you are not worth remembering.",
        },
        {
            "type": "prose",
            "text": "That is almost worse.",
        },
        {
            "type": "stat",
            "changes": {"health": -20},
        },
        {
            "type": "flag",
            "key":   "guards_forced",
            "value": True,
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_GUARDS = {
    "beats": [
        {
            "type": "italic",
            "text": "Their faces are familiar. Not known — familiar. The way a word "
                    "is familiar before you remember its meaning.",
        },
        {
            "type": "prose",
            "text": "You have seen men stand like this. You have stood like this. "
                    "There is something in the angle of the shoulders, the particular "
                    "stillness, that belongs to a specific kind of training.",
        },
        {
            "type": "italic",
            "text": "Gunnar's men stood like this.",
        },
        {
            "type": "memory",
            "key":   "guards_recognised",
            "label": "Where you have seen that stillness before",
            "text":  "The guards at the gate. The angle of their shoulders. "
                     "The particular stillness of men trained by the same hand.",
        },
        {
            "type": "flag",
            "key":   "guards_examined",
            "value": True,
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_COURTYARD = {
    "beats": [
        {
            "type": "prose",
            "text": "Beyond the gate is a courtyard. Cobblestones. A well. Three "
                    "buildings and a tower. Everything is exactly where it should be.",
        },
        {
            "type": "italic",
            "text": "Nothing is where it feels like it should be.",
        },
        {
            "type": "prose",
            "text": "A horse stands at a hitching post, saddled and ready. A bucket "
                    "of water beside it, full. Three soldiers cross the courtyard "
                    "frozen mid-step — one looking down, one looking up, one looking "
                    "directly at you.",
        },
        {
            "type": "italic",
            "text": "The one looking at you has been looking at you since before "
                    "you arrived.",
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_WALL = {
    "beats": [
        {
            "type": "prose",
            "text": "You press your palm flat against the stone.",
        },
        {
            "type": "italic",
            "text": "It is warm. Warmer than the torch explains. Warmer than stone "
                    "should be.",
        },
        {
            "type": "prose",
            "text": "Not the warmth of sun-heated rock. The warmth of something "
                    "held. Something that has not been released.",
        },
        {
            "type": "memory",
            "key":   "wall_warmth",
            "label": "Something about warmth in the wrong place",
            "text":  "The stone of the gatehouse wall. How warm it was. "
                     "What kind of warmth that was.",
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_INSIDE = {
    "beats": [
        {
            "type": "prose",
            "text": "The courtyard is silent in the way the battlefield was silent — "
                    "completely, without apology. But the battlefield was empty. "
                    "This is not empty.",
        },
        {
            "type": "prose",
            "text": "The smell of food reaches you before anything else. "
                    "Real food, recently cooked. "
                    "Light under the door of the Great Hall ahead. "
                    "Warmth where there should be cold.",
        },
        {
            "type": "prose",
            "text": "And a voice, low and even, speaking to no one visible:",
        },
        {
            "type": "italic",
            "text": "\"I wondered which door you would use.\"",
        },
    ],
    "next": "great_hall_entrance",
}

# ═════════════════════════════════════════════════════════════
#  ACT II — THE GREAT HALL / ODRIK
# ═════════════════════════════════════════════════════════════

SCENE_GREAT_HALL_ENTRANCE = {
    "header": {
        "title":    "THE GREAT HALL",
        "subtitle": "everything is exactly as it was left",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "The Great Hall is wrong in the same way everything here is wrong — "
                "perfectly preserved, perfectly still, "
                "perfectly the moment before something happened."
            ),
        },
        {
            "type": "prose",
            "text": (
                "Forty men sit at the long tables. "
                "Cups raised, mouths open, faces turned toward each other "
                "in the specific geometry of interrupted conversation. "
                "The food on the tables is real. "
                "The smell of it reaches you in waves — "
                "roast meat, bread, something sweet. "
                "None of it has spoiled. "
                "None of it ever will."
            ),
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: not s.flags.get("odrik_met"),
                    "text": (
                        "At the far end, alone at the head table, "
                        "sits one man who is not frozen."
                    ),
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: not s.flags.get("odrik_met"),
                    "text": (
                        "He is not young. Fifty, perhaps — "
                        "the kind of man who has spent fifty years "
                        "acquiring a precise and careful stillness. "
                        "A dark robe, ink-stained at the cuffs. "
                        "A cup in front of him, untouched. "
                        "His eyes are on the table."
                    ),
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: not s.flags.get("odrik_met"),
                    "text": (
                        "He already knew you were in the room "
                        "before you crossed the threshold."
                    ),
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: not s.flags.get("odrik_met"),
                    "text": (
                        "He does not look up when you approach. "
                        "He speaks first."
                    ),
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: not s.flags.get("odrik_met"),
                    "text": (
                        "\"You came alone,\" he says. "
                        "\"I did not know if you would come alone.\""
                    ),
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: not s.flags.get("odrik_met"),
                    "text": (
                        "A pause. He is listening to something — "
                        "the quality of your footsteps, perhaps, "
                        "or the silence you bring with you."
                    ),
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: not s.flags.get("odrik_met"),
                    "text": "\"You fought the Sentinel.\"",
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: not s.flags.get("odrik_met"),
                    "text": "Still he does not look up.",
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: not s.flags.get("odrik_met"),
                    "text": (
                        "\"I heard the bell stop. "
                        "I have been listening for that sound "
                        "for a very long time.\""
                    ),
                },
            ],
        },
    ],
    "choices": [
        {
            "label": "Say nothing. Wait.",
            "next":  "odrik_silence",
            "condition": lambda s: not s.flags.get("odrik_met"),
        },
        {
            "label": "\"Then you knew I was coming.\"",
            "next":  "odrik_knew",
            "condition": lambda s: not s.flags.get("odrik_met"),
        },
        {
            "label": "\"What are you?\"",
            "next":  "odrik_what_are_you",
            "condition": lambda s: not s.flags.get("odrik_met"),
        },
        {
            "label": "Examine the door frame.",
            "next":  "great_hall_rune_door",
            "condition": lambda s: (
                s.flags.get("odrik_met") and
                s.flags.get("odrik_place_seen") and
                s.has_memory("odrik_purpose") and
                s.has_memory("the_key_origin") and
                not s.flags.get("rune_door_seen")
            ),
        },
        {
            "label": "Return to Odrik.",
            "next":  "odrik_first_questions",
            "condition": lambda s: s.flags.get("odrik_met"),
        },
    ],
}

SCENE_ODRIK_SILENCE = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "You say nothing. "
                "You have learned, in this place, "
                "that silence is sometimes the most honest answer."
            ),
        },
        {
            "type": "prose",
            "text": "He looks up.",
        },
        {
            "type": "italic",
            "text": (
                "\"Good,\" he says. "
                "Not approval, exactly. "
                "More like confirmation of something he suspected."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"Gunnar said you listened before you spoke. "
                "Most people don't. "
                "It is why he trusted you.\""
            ),
        },
        {
            "type": "prose",
            "text": (
                "He says Gunnar's name the way you say the name "
                "of someone you have been thinking about "
                "for a very long time. "
                "Carefully. Like it still has weight."
            ),
        },
    ],
    "next": "odrik_measures_you",
}

SCENE_ODRIK_KNEW = {
    "beats": [
        {
            "type": "prose",
            "text": "He looks up for the first time.",
        },
        {
            "type": "italic",
            "text": (
                "\"I knew someone would come,\" he says. "
                "\"I did not know it would be you "
                "until the Sentinel stopped.\""
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"That thing tests what belongs here "
                "and what does not. "
                "The dead belong here — they cannot leave. "
                "The living do not belong — they cannot enter. "
                "You are neither.\""
            ),
        },
        {
            "type": "prose",
            "text": (
                "He says this without drama. "
                "It is an observation, not an accusation."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"That narrows it considerably,\" "
                "he says. \"To one person.\""
            ),
        },
    ],
    "next": "odrik_measures_you",
}

SCENE_ODRIK_WHAT_ARE_YOU = {
    "beats": [
        {
            "type": "prose",
            "text": "That makes him look up.",
        },
        {
            "type": "italic",
            "text": (
                "\"An interesting first question,\" he says. "
                "Not pleased, not offended. "
                "Noting it."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"I am Odrik. I was Gunnar's adviser "
                "for eleven years. "
                "I followed him to this valley "
                "because he asked me to.\""
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"What I am now — "
                "that is a more difficult question. "
                "I have had considerable time to consider it "
                "and I do not yet have a satisfying answer.\""
            ),
        },
        {
            "type": "prose",
            "text": (
                "He looks at you steadily. "
                "He is deciding something."
            ),
        },
    ],
    "next": "odrik_measures_you",
}

SCENE_ODRIK_MEASURES_YOU = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "He looks at you properly now. "
                "Not at your face — at everything else. "
                "Your hands. What you carry. "
                "The way you are standing."
            ),
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: s.equipped_weapon == "Gunnar's Axe",
                    "text": (
                        "His eyes stop at the axe on your belt. "
                        "Gunnar's axe. "
                        "He would know it anywhere — "
                        "he watched Gunnar carry it for eleven years."
                    ),
                },
                {
                    "condition": None,
                    "text": (
                        "His eyes move across what you carry. "
                        "He catalogues it without expression."
                    ),
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": lambda s: s.equipped_weapon == "Gunnar's Axe",
                    "text": (
                        "\"He gave it to you,\" Odrik says. "
                        "Flat. Careful. "
                        "\"Or you took it.\""
                    ),
                },
                {
                    "condition": None,
                    "text": (
                        "\"You have been on the battlefield,\" "
                        "he says. \"You found things.\""
                    ),
                },
            ],
        },
        {
            "type": "italic",
            "text": (
                "\"Sit down,\" he says. "
                "\"I will answer what I can. "
                "I cannot promise it will be everything.\""
            ),
        },
        {
            "type": "flag",
            "key":   "odrik_met",
            "value": True,
        },
    ],
    "next": "odrik_first_questions",
}

SCENE_ODRIK_FIRST_QUESTIONS = {
    "header": {
        "title":    "ODRIK THE BOUND",
        "subtitle": "he will answer what he can",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "He turns the cup in his hands without drinking. "
                "A habit — something to do with his hands "
                "while he chooses his words."
            ),
        },
    ],
    "choices": [
        {
            "label": "\"What is this place?\"",
            "next":  "odrik_explains_place",
        },
        {
            "label": "Show him the key. \"The rune is incomplete.\"",
            "next":  "odrik_the_night",
            "condition": lambda s: (
                s.flags.get("rune_door_seen") and
                not s.flags.get("odrik_night_confronted")
            ),
        },
        {
            "label": "\"What does the key open?\"",
            "next":  "odrik_the_key",
            "condition": lambda s: "Remembrance Key" in s.inventory,
        },
        {
            "label": "\"Why are you still here?\"",
            "next":  "odrik_why_bound",
        },
        {
            "label": "\"Why can't you tell me?\"",
            "next":  "odrik_go_forward",
            "condition": lambda s: (
                s.flags.get("odrik_night_confronted") and
                not s.flags.get("odrik_sent_forward")
            ),
        },
        {
            "label": "Leave Odrik for now. Look around the hall.",
            "next":  "great_hall_entrance",
        },
    ],
}

SCENE_ODRIK_EXPLAINS_PLACE = {
    "beats": [
        {
            "type": "italic",
            "text": (
                "\"It is a place between,\" he says. "
                "\"Between dying and being dead. "
                "Between what happened and what it meant.\""
            ),
        },
        {
            "type": "prose",
            "text": (
                "He looks at the frozen men around them."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"They are held here. "
                "Not imprisoned — held. "
                "There is a difference. "
                "A prison keeps you against your will. "
                "This holds you because something is unfinished. "
                "Something they were part of "
                "that has not resolved.\""
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"The battlefield. The longhouse. "
                "This hall. "
                "All of it is the same thing — "
                "a moment that refuses to end "
                "because it was not allowed to end properly.\""
            ),
        },
        {
            "type": "prose",
            "text": (
                "He says this as if reciting something "
                "he has worked out slowly, "
                "over a long time, "
                "in a room where no one else could hear."
            ),
        },
        {
            "type": "italic",
            "text": "\"You are here to end it.\"",
        },
        {
            "type": "prose",
            "text": (
                "Not a question. "
                "But not entirely certain either."
            ),
        },
        {
            "type": "flag",
            "key":   "odrik_place_seen",
            "value": True,
        },
    ],
    "next": "odrik_first_questions",
}

SCENE_ODRIK_THE_NIGHT = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "You hold out the key. "
                "Not as a threat — you let him see it."
            ),
        },
        {
            "type": "prose",
            "text": "Odrik looks at it. He does not move.",
        },
        {
            "type": "prose",
            "text": (
                "And then something shifts in him — "
                "not in his face, not in his hands. "
                "Deeper than that. "
                "As if a structure beneath him trembles."
            ),
        },
        {
            "type": "italic",
            "text": "It lasts one breath. Then he is himself again.",
        },
        {
            "type": "italic",
            "text": "\"The rune is incomplete.\"",
        },
        {
            "type": "prose",
            "text": (
                "He looks at you for the first time "
                "without first calculating."
            ),
        },
        {
            "type": "italic",
            "text": "\"Then why does it hold?\"",
        },
        {
            "type": "prose",
            "text": "You know the answer. You saw it in the door frame.",
        },
        {
            "type": "italic",
            "text": "\"Because something else is finishing it.\"",
        },
        {
            "type": "prose",
            "text": "Silence.",
        },
        {
            "type": "prose",
            "text": (
                "Odrik sets the cup down. "
                "He has not set it down once until now."
            ),
        },
        {
            "type": "memory",
            "key":   "rune_not_alone",
            "label": "What the rune is connected to",
            "text":  (
                "The rune at the door is incomplete. And yet it holds. "
                "Because something else is finishing it. "
                "You said it before you fully understood it. "
                "Odrik set down the cup."
            ),
        },
        {
            "type": "flag",
            "key":   "odrik_night_confronted",
            "value": True,
        },
    ],
    "next": "odrik_first_questions",
}

SCENE_ODRIK_THE_KEY = {
    "beats": [
        {
            "type": "prose",
            "text": "He goes very still.",
        },
        {
            "type": "italic",
            "text": (
                "\"Show me.\""
            ),
        },
        {
            "type": "prose",
            "text": (
                "You hold it out. "
                "He does not touch it — "
                "he leans forward and looks at it the way "
                "a man looks at something "
                "he thought was lost."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"I made that,\" he says quietly. "
                "\"Eleven years ago. "
                "Before any of this. "
                "Before I knew what it would be needed for.\""
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"It is not a key to a place. "
                "It is a key to a memory — "
                "specifically, to yours. "
                "It was made from something of yours "
                "that Gunnar kept. "
                "Something you gave him "
                "the night you swore the oath.\""
            ),
        },
        {
            "type": "prose",
            "text": (
                "He sits back. "
                "He is watching your face."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"You don't remember giving it to him,\" "
                "he says. \"Not yet. "
                "You will.\""
            ),
        },
        {
            "type": "memory",
            "key":   "the_key_origin",
            "label": "What the key is made from",
            "text":  (
                "Odrik made it. Eleven years ago. "
                "From something you gave Gunnar "
                "the night you swore the oath. "
                "Something you no longer remember giving."
            ),
        },
    ],
    "next": "odrik_first_questions",
}

SCENE_GREAT_HALL_RUNE_DOOR = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "You stop at the door frame. "
                "You are not sure why — something in the way the light falls here, "
                "or does not fall. Something that made you slow down."
            ),
        },
        {
            "type": "prose",
            "text": (
                "Then you see them. "
                "Runes, cut into the stone on both sides of the frame. "
                "Cut too deep — deeper than any blade should reach. "
                "The stone around them has not cracked, has not splintered. "
                "Whatever made these marks was not cutting. "
                "It was insisting."
            ),
        },
        {
            "type": "italic",
            "text": "They do not form a complete circle.",
        },
        {
            "type": "prose",
            "text": (
                "And yet they hold. "
                "You can feel it — something in the air around the frame "
                "that is not quite pressure, not quite warmth. "
                "A shape that completes itself in a medium you cannot see."
            ),
        },
        {
            "type": "italic",
            "text": (
                "As if the pattern continues beyond what the eye can follow."
            ),
        },
        {
            "type": "prose",
            "text": "This was not made to seal something away.",
        },
        {
            "type": "italic",
            "text": "It was made to keep something in place.",
        },
        {
            "type": "memory",
            "key":   "rune_door",
            "label": "What is holding the hall together",
            "text":  (
                "The runes at the door frame. Cut too deep, incomplete, and yet — "
                "they hold. Not a seal. Not a lock. "
                "A structure that keeps the moment from ending. "
                "Someone made this. Someone who knew exactly what they were doing."
            ),
        },
        {
            "type": "flag",
            "key":   "rune_door_seen",
            "value": True,
        },
    ],
    "next": "great_hall_entrance",
}

SCENE_ODRIK_WHY_BOUND = {
    "beats": [
        {
            "type": "italic",
            "text": (
                "\"Because I have not done "
                "what I came here to do,\" he says."
            ),
        },
        {
            "type": "prose",
            "text": (
                "He says it simply. "
                "Not with self-pity — "
                "more the way you state a fact "
                "that has been true for a long time "
                "and that you have made your peace with."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"I came to this valley as Gunnar's adviser. "
                "My purpose was to prevent what happened. "
                "I failed. "
                "I knew I had failed while it was still happening "
                "and I could not stop it.\""
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"The binding is not a punishment. "
                "It is an unfinished sentence. "
                "I cannot leave until the sentence is finished.\""
            ),
        },
        {
            "type": "prose",
            "text": (
                "He looks at you steadily."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"You finishing it "
                "and me finishing it "
                "are the same thing. "
                "That is why I have been waiting for you.\""
            ),
        },
        {
            "type": "memory",
            "key":   "odrik_purpose",
            "label": "Why Odrik is bound",
            "text":  (
                "He came to prevent what happened. "
                "He failed. "
                "The binding is an unfinished sentence — "
                "he cannot leave until it ends. "
                "Your ending it and his ending it "
                "are the same thing."
            ),
        },
    ],
    "next": "odrik_first_questions",
}

SCENE_ODRIK_GO_FORWARD = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "He looks at where the cup was. "
                "As if its absence means something."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"I was there. I saw all of it.\""
            ),
        },
        {
            "type": "prose",
            "text": "A pause.",
        },
        {
            "type": "italic",
            "text": (
                "\"There are things I cannot say. "
                "Not because I choose silence — "
                "the binding holds those words. "
                "They exist in me but they cannot come out.\""
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"But they exist somewhere else too. "
                "In this building. "
                "In what was left behind.\""
            ),
        },
        {
            "type": "prose",
            "text": (
                "He meets your eyes."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"The rune is not alone. "
                "Follow what it is connected to.\""
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"You will find out what happened. "
                "Not from me. "
                "From the place itself.\""
            ),
        },
        {
            "type": "flag",
            "key":   "odrik_sent_forward",
            "value": True,
        },
    ],
    "next": "great_hall_entrance",
}

SCENES = {
    "name_entry":                SCENE_NAME_ENTRY,
    "awakening":                 SCENE_AWAKENING,
    "find_weapon":               SCENE_FIND_WEAPON,
    "battlefield_open":          SCENE_BATTLEFIELD_OPEN,
    "battlefield_look_around":   SCENE_BATTLEFIELD_LOOK_AROUND,
    "soul_leif":                 SCENE_SOUL_LEIF,
    "leif_gives_name":        SCENE_LEIF_GIVES_NAME,
    "leif_the_oath":          SCENE_LEIF_THE_OATH,
    "leif_gunnar_intro":      SCENE_LEIF_GUNNAR_INTRO,
    "leif_farewell":          SCENE_LEIF_FAREWELL,
    "leif_mercy_kill":        SCENE_LEIF_MERCY_KILL,
    "leif_defense":           SCENE_LEIF_DEFENSE,
    "leif_battle_account":    SCENE_LEIF_BATTLE_ACCOUNT,
    "leif_survivors":         SCENE_LEIF_SURVIVORS,
    "longhouse_ruins":        SCENE_LONGHOUSE_RUINS,
    "cairn_rest":             SCENE_CAIRN_REST,
    "forge_search":           SCENE_FORGE_SEARCH,
    "scavenge_east":          SCENE_SCAVENGE_EAST,
    "combat_draugar_east":    SCENE_COMBAT_DRAUGAR_EAST,
    "scavenge_east_after":    SCENE_SCAVENGE_EAST_AFTER,
    "the_mound":              SCENE_THE_MOUND,
    "gunnar_dialogue_peace":  SCENE_GUNNAR_DIALOGUE_PEACE,
    "gunnar_dialogue_challenge": SCENE_GUNNAR_DIALOGUE_CHALLENGE,
    "gunnar_dialogue_truth":  SCENE_GUNNAR_DIALOGUE_TRUTH,
    "combat_gunnar":          SCENE_COMBAT_GUNNAR,
    "act1_end":             SCENE_ACT1_END,
    "final_rest":             SCENE_FINAL_REST,
    "act_2_intro":            SCENE_ACT_2_INTRO,
    # Act II — The Stirring Beneath
    "fog_road":               SCENE_FOG_ROAD,
    "fog_the_held":           SCENE_FOG_THE_HELD,
    "fog_held_other":         SCENE_FOG_HELD_OTHER,
    "fog_held_release":       SCENE_FOG_HELD_RELEASE,
    "fog_held_after":         SCENE_FOG_HELD_AFTER,
    "fog_sentinel":           SCENE_FOG_SENTINEL,
    "fog_sentinel_wait":      SCENE_FOG_SENTINEL_WAIT,
    "fog_sentinel_avoided":   SCENE_FOG_SENTINEL_AVOIDED,
    "combat_fog_sentinel":    SCENE_COMBAT_FOG_SENTINEL,
    "fog_sentinel_after":     SCENE_FOG_SENTINEL_AFTER,
    "gatehouse_approach":     SCENE_GATEHOUSE_APPROACH,
    "gatehouse_guards":       SCENE_GATEHOUSE_GUARDS,
    "gatehouse_guards_hostile": SCENE_GATEHOUSE_GUARDS_HOSTILE,
    "gatehouse_guards_calmed":  SCENE_GATEHOUSE_GUARDS_CALMED,
    "gatehouse_guards_spoken":  SCENE_GATEHOUSE_GUARDS_SPOKEN,
    "gatehouse_guards_axe":     SCENE_GATEHOUSE_GUARDS_AXE,
    "gatehouse_guards_forced":  SCENE_GATEHOUSE_GUARDS_FORCED,
    "gatehouse_courtyard":    SCENE_GATEHOUSE_COURTYARD,
    "gatehouse_wall":         SCENE_GATEHOUSE_WALL,
    "gatehouse_inside":       SCENE_GATEHOUSE_INSIDE,
    # Act II — The Great Hall / Odrik
    "great_hall_entrance":    SCENE_GREAT_HALL_ENTRANCE,
    "great_hall_rune_door":   SCENE_GREAT_HALL_RUNE_DOOR,
    "odrik_silence":          SCENE_ODRIK_SILENCE,
    "odrik_knew":             SCENE_ODRIK_KNEW,
    "odrik_what_are_you":     SCENE_ODRIK_WHAT_ARE_YOU,
    "odrik_measures_you":     SCENE_ODRIK_MEASURES_YOU,
    "odrik_first_questions":  SCENE_ODRIK_FIRST_QUESTIONS,
    "odrik_explains_place":   SCENE_ODRIK_EXPLAINS_PLACE,
    "odrik_the_night":        SCENE_ODRIK_THE_NIGHT,
    "odrik_the_key":          SCENE_ODRIK_THE_KEY,
    "odrik_why_bound":        SCENE_ODRIK_WHY_BOUND,
    "odrik_go_forward":       SCENE_ODRIK_GO_FORWARD,
}
