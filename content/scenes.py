# ============================================================
#  content/scenes.py
#  All scenes for Act 1 — The Battlefield of Silence.
#  Pure data. No logic. The engine in scene.py runs these.
# ============================================================

# ─────────────────────────────────────────────────────────────
#  AWAKENING
# ─────────────────────────────────────────────────────────────
SCENE_AWAKENING = {
    "header": {
        "title":    "FORGOTTEN AMONG THE FALLEN",
        "subtitle": "A Viking Dark Fantasy",
    },
    "show_hud": False,
    "beats": [
        {"type": "separator", "style": "rune"},
        {"type": "delay", "seconds": 0.8},
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
        {"type": "pause"},
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
        {"type": "pause"},
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
    "next": "battlefield_open",
}

# ─────────────────────────────────────────────────────────────
#  BATTLEFIELD — OPEN
# ─────────────────────────────────────────────────────────────
SCENE_BATTLEFIELD_OPEN = {
    "header": {
        "title":    "THE BATTLEFIELD OF SILENCE",
        "subtitle": "Zone 1 — The Waking Field",
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
            "label":     "Pull the arrow. End it quickly.",
            "next":      "leif_mercy_kill",
            "effects":   {"mercy": 8, "resolve": -5},
            "narration": (
                "It is mercy. You tell yourself it is mercy. "
                "His eyes thank you before they close."
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
            "type": "memory",
            "key":   "the_broken_oath",
            "label": "The night of the eastern ridge",
            "text":  (
                "You were not there. You do not yet know why. "
                "But the shape of the absence is beginning to form."
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
            "text": '"He will find you," Leif says. "He always finds those who owe him a debt. Go to the mound first. Rest. There is a cairn — it still burns."',
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
                "You scan the field. The fog shifts. "
                "To the north, the longhouse ruins you have not yet searched. "
                "To the east, the dense dead. "
                "One of them moved, earlier. You remember that."
            )
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
            "label":     "Return to the battlefield.",
            "next":      "battlefield_open",
        },
    ],
}

SCENE_LEIF_FAREWELL = {
    "beats": [
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
                "It is quick. He lets it be quick. "
                "You hold the weight of it for a moment, "
                "then set it down somewhere in your chest where you keep things "
                "that have no other place to go."
            )
        },
        {
            "type": "prose",
            "text": (
                "You search him out of necessity. "
                "He carries a small knife, a pouch of echo dust, and a piece of birchbark "
                "with a name scratched into it. "
                "The name is yours."
            )
        },
        {
            "type": "item",  "item": "Leif's knife",     "action": "give"},
        {"type": "shards", "amount": 45},
        {
            "type": "memory",
            "key":   "my_name",
            "label": "Your name, on a dead man's birchbark",
            "text":  (
                "He knew your name. He carried it with him into the battle. "
                "You do not know yet whether that makes the weight lighter or heavier."
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
                "You sit. The cairn's warmth spreads through your back. "
                "You do not sleep — you are not certain you can sleep — "
                "but you close your eyes and let the memory try to find you."
            )
        },
        {"type": "delay", "seconds": 1.5},
        {
            "type": "italic",
            "text": "A hall. Firelight. A voice you know better than your own saying your name with something that might be disappointment. Or grief.",
            },
        {"type": "pause"},
        {
            "type": "prose",
            "text": "You open your eyes. The fog is the same. But you feel more solid in it."
        },
    ],
    "next": "battlefield_open",
}

SCENE_FORGE_SEARCH = {
    "beats": [
        {
            "type": "prose",
            "text": (
                "The forge yields more than you expected. "
                "Someone was working here close to the end — "
                "there are half-finished repairs, a blade still in the vice, "
                "and a small hoard of iron scraps that survived the collapse."
            )
        },
        {"type": "item",   "item": "iron scraps",    "action": "give"},
        {"type": "item",   "item": "whetstone",      "action": "give"},
        {"type": "shards", "amount": 80},
        {
            "type": "prose",
            "text": (
                "There is also a piece of cloth, wrapped around something small. "
                "You unwrap it. A medallion — clan mark, though which clan "
                "you cannot quite read. "
                "The style is familiar. "
                "The familiarity is the kind that hurts."
            )
        },
        {
            "type": "memory",
            "key":   "the_medallion",
            "label": "A clan medallion, familiar and nameless",
            "text":  (
                "You have seen this mark before. "
                "You have worn it. "
                "You are certain of it — the weight of it in your hand is the weight "
                "of something you once carried every day."
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
        {
            "type": "prose",
            "text": (
                "The battlefield settles again. "
                "You stand in it, breathing. "
                "The quiet after violence is a specific kind of quiet. "
                "You recognise it."
            )
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
            "label": "Take the Remembrance Key. Prepare to move on.",
            "next":  "zone_1_end",
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  ZONE 1 END
# ─────────────────────────────────────────────────────────────
SCENE_ZONE_1_END = {
    "header": {
        "title":    "SILENCE FALLS",
        "subtitle": "The Battlefield of Silence — cleared",
    },
    "beats": [
        {"type": "item", "item": "Remembrance Key", "action": "give"},
        {
            "type": "prose",
            "text": (
                "Gunnar is still. "
                "Not gone — you do not think he can be gone — "
                "but still, in the way that a long argument is still "
                "when both sides run out of words. "
                "For now, that is enough."
            )
        },
        {
            "type": "prose",
            "text": (
                "You stand on the mound and look at the battlefield. "
                "Ten thousand dead and one of them is you. "
                "You have been walking among them long enough "
                "that the distinction has started to feel academic."
            )
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
        {"type": "separator", "style": "rune"},
        {
            "type": "prose",
            "text": (
                "To the south, the fog is thinner. "
                "Through it you can see the shape of mountains — "
                "or what your memory insists are mountains, "
                "though they have no peaks and do not end. "
                "The Remembrance Key is cold in your hand. "
                "Whatever it opens is through there."
            )
        },
        {"type": "pause", "msg": "  [ Act 1 complete — press enter ]"},
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
    "beats": [
        {
            "type": "prose",
            "text": (
                "You go back to the cairn. "
                "You sit. You close your eyes. "
                "The memory comes closer — not all the way, but closer. "
                "You can see the eastern ridge now. "
                "You can see why you were not there. "
                "You are not yet ready to say it out loud."
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
        {"type": "separator", "style": "rune"},
        {
            "type": "prose",
            "text": "The fog to the south is colder. That is the only difference, at first.",
        },
        {"type": "delay", "seconds": 1.0},
        {
            "type": "italic",
            "text": "To be continued.",
        },
        {"type": "separator", "style": "rune"},
        {"type": "delay", "seconds": 1.0},
    ],
    "choices": [
        {
            "label":     "Save and quit.",
            "next":      "__save_quit__",
        },
        {
            "label":     "Return to the battlefield (restart Act 1).",
            "next":      "__restart__",
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  SCENE REGISTRY
# ─────────────────────────────────────────────────────────────
SCENES = {
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
    "zone_1_end":             SCENE_ZONE_1_END,
    "final_rest":             SCENE_FINAL_REST,
    "act_2_intro":            SCENE_ACT_2_INTRO,
}
