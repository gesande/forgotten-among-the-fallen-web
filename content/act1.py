# ============================================================
#  content/act1.py
#  Act I — The Battlefield of Silence
#  Pure data. No logic. The engine in scene_web.py runs these.
# ============================================================

# ─────────────────────────────────────────────────────────────
#  AWAKENING
# ─────────────────────────────────────────────────────────────
# ── Name entry: shown first, before any choices ──────────────
SCENE_NAME_ENTRY = {
    "art": "name_entry",
    "header": {
        "title": "FORGOTTEN AMONG THE FALLEN",
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
            ),
        },
        {
            "type": "prose",
            "text": (
                "The sky above is the colour of an old bruise. "
                "No crows. No flies. No sound but the wind moving through the dead. "
                "You look at your hands. They are yours. "
                "You look at the bodies. They are not moving. "
                "Not yet."
            ),
        },
        {
            "type": "prose",
            "text": (
                "A name sits at the edge of your memory like a word in a language "
                "you used to speak. You reach for it."
            ),
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
    "art": "battlefield",
    "header": {
        "title": "THE WAKING FIELD",
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
            ),
        },
        {
            "type": "prose",
            "text": (
                "You do not know how long you have been lying among them. "
                "You do not know why you rose when they did not. "
                "You know your name — the fog gave that back to you, at least — "
                "but everything else sits just beyond reach, "
                "like words in a language you are forgetting."
            ),
        },
        {
            "type": "italic",
            "text": (
                "Somewhere to the north, the ruins of a longhouse. "
                "To the east, the dead lie thicker — the fighting was hardest there. "
                "To the south, a burial mound rises from the earth like a held breath. "
                "And somewhere nearby, you can hear something. "
                "A voice, or what is left of one."
            ),
        },
    ],
    "choices": [
        {
            "label": "Stand still. Listen. Try to understand where you are.",
            "next": "battlefield_open",
            "effects": {"resolve": 5},
            "narration": (
                "You breathe. Slowly. The fog shifts around you. "
                "You are alive — or something close enough to alive that the difference "
                "does not matter yet."
            ),
        },
        {
            "label": "Move. Find someone. Find anything still breathing.",
            "next": "battlefield_open",
            "effects": {"resolve": -3, "brutality": 2},
            "narration": (
                "You start walking before you have decided where. "
                "Somewhere in the fog, something shifts. "
                "It might be the wind."
            ),
        },
        {
            "label": "Look for a weapon. Whatever happened, you will not face it unarmed.",
            "next": "find_weapon",
            "effects": {"brutality": 5},
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
    "art": "battlefield",
    "show_hud": False,
    "beats": [
        {
            "type": "prose",
            "text": (
                "You pull an axe from the mud. "
                "The handle is cracked, the head rusted to the colour of dried blood. "
                "It is heavier than you remember axes being — "
                "though you cannot yet say what you remember."
            ),
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
            ),
        },
        {
            "type": "memory",
            "key": "the_weapon_grip",
            "label": "How I hold a weapon before the battle",
            "text": (
                "The thumb runs along the edge to test it. The wrist turns once, "
                "checking the balance. You did not decide to do these things. "
                "Your body did them — the way it has done them "
                "every morning of every campaign you no longer remember."
            ),
        },
    ],
    "choices": [
        {
            "label": "Grip it tight. Step forward.",
            "next": "battlefield_open",
            "effects": {"brutality": 2},
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  BATTLEFIELD — OPEN
# ─────────────────────────────────────────────────────────────
SCENE_BATTLEFIELD_OPEN = {
    "art": "battlefield",
    "header": {
        "title": "THE BATTLEFIELD OF SILENCE",
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
            ),
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": {"stat_gte": "curse_stacks", "value": 2},
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
            ],
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
            ),
        },
    ],
    "choices": [
        {
            "label": "Go to the man against the shield-wall.",
            "next": "soul_leif",
            "condition": {"not": {"flag": "leif_done"}},
        },
        {
            "label": "Search the longhouse ruins to the north.",
            "next": "longhouse_ruins",
            "effects": {"resolve": 2},
            "condition": {"not": {"flag": "found_forge"}},
        },
        {
            "label": "Search the forge again.",
            "next": "forge_search",
            "condition": {
                "and": [{"flag": "found_forge"}, {"not": {"flag": "forge_searched"}}]
            },
        },
        {
            "label": "Return to the longhouse ruins.",
            "next": "longhouse_ruins",
            "condition": {"and": [{"flag": "found_forge"}, {"flag": "forge_searched"}]},
        },
        {
            "label": "Move east into the dense dead. Scavenge.",
            "next": "scavenge_east",
            "effects": {"brutality": 3},
            "condition": {"not": {"flag": "east_searched"}},
        },
        {
            "label": "Go south — towards the mound.",
            "next": "the_mound",
            "condition": {"or": [{"flag": "found_forge"}, {"flag": "east_searched"}]},
        },
        {
            "label": "Look around. There must be more here.",
            "next": "battlefield_look_around",
            "condition": {
                "and": [
                    {"not": {"flag": "found_forge"}},
                    {"not": {"flag": "east_searched"}},
                    {"flag": "leif_done"},
                ]
            },
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  SOUL: LEIF — The Dying Soldier
# ─────────────────────────────────────────────────────────────
SCENE_SOUL_LEIF = {
    "art": "leif",
    "header": {
        "title": "THE DYING SOLDIER",
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
            ),
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
            ),
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
            "label": '"Tell me what happened here."',
            "next": "leif_battle_account",
            "effects": {"resolve": 3},
        },
        {
            "label": '"Tell me my name."',
            "next": "leif_gives_name",
            "effects": {"resolve": 5},
        },
        {
            "label": '"Who is still alive?"',
            "next": "leif_survivors",
            "effects": {"honour": 3},
        },
        {
            "label": "He is dying. Stay with him until he is gone.",
            "next": "leif_mercy_kill",
            "effects": {"mercy": 8, "honour": 5},
            "narration": (
                "You do not leave. That is all. " "Sometimes that is enough."
            ),
        },
    ],
}

SCENE_LEIF_GIVES_NAME = {
    "art": "leif",
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
            ),
        },
        {
            "type": "memory",
            "key": "my_name",
            "label": "Your name, spoken by a dying man",
            "text": (
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
            "label": '"What did I do?"',
            "next": "leif_the_oath",
        },
        {
            "label": '"Who is Gunnar?"',
            "next": "leif_gunnar_intro",
        },
        {
            "label": "Do not ask. You are not certain you want to know.",
            "next": "leif_farewell",
            "effects": {"resolve": -5},
        },
    ],
}

SCENE_LEIF_THE_OATH = {
    "art": "leif",
    "beats": [
        {
            "type": "italic",
            "text": (
                '"You broke the oath," Leif says. '
                '"The oath of the drengr. '
                "You swore to stand at Gunnar's shield. "
                "On the last night, when the Svear came from the eastern ridge — "
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
            ),
        },
        {
            "type": "italic",
            "text": (
                '"I always thought," Leif says quietly, "that there was a reason. '
                "Not cowardice — I knew you four years, and you were not a coward. "
                "A debt, maybe. Something you found out. "
                "Something about Gunnar that you could not live with "
                'and could not say out loud."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"Whatever it was — it was enough for you. '
                "Whether it was enough to justify it... "
                'that is a different question."'
            ),
        },
        {
            "type": "memory",
            "key": "the_broken_oath",
            "label": "The night of the eastern ridge",
            "text": (
                "You were not there. You do not yet know why. "
                "But Leif's guess sits in you like an ember — "
                "not because it is right, but because it is close enough to feel warm."
            ),
        },
    ],
    "choices": [
        {
            "label": '"Where is Gunnar now?"',
            "next": "leif_gunnar_intro",
        },
        {
            "label": '"I had a reason."',
            "next": "leif_defense",
            "effects": {"honour": -5, "resolve": 5},
        },
        {
            "label": "Say nothing. There is nothing to say.",
            "next": "leif_farewell",
            "effects": {"honour": 5, "resolve": -3},
        },
    ],
}

SCENE_LEIF_GUNNAR_INTRO = {
    "art": "leif",
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
                "Leif's breath is shallow now. Each one is a decision. "
                "He has made his peace with the final one."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"Go to the mound. He will be there. '
                "And go to the cairn first — it still burns. "
                'Whatever you owe Gunnar, do not face it on empty ground."'
            ),
        },
    ],
    "choices": [
        {
            "label": '"Thank you, Leif."',
            "next": "leif_farewell",
            "effects": {"honour": 5, "mercy": 3},
        },
        {
            "label": "Leave without a word. The dead do not need courtesy.",
            "next": "leif_ambush",
            "effects": {"honour": -3, "brutality": 2},
            "flags": {"leif_done": True},
        },
    ],
}

# Fallback scene — shown when player has talked to Leif but not yet
# explored enough to unlock the mound path
SCENE_BATTLEFIELD_LOOK_AROUND = {
    "art": "battlefield",
    "beats": [
        {
            "type": "prose",
            "text": (
                "You stop and take stock. The fog shifts but does not clear. "
                "You have learned to read this battlefield the way you would read a room — "
                "what is present, what is missing, what has been moved."
            ),
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": {
                        "and": [
                            {"flag": "found_forge"},
                            {"flag": "east_searched"},
                            {"flag": "leif_done"},
                        ]
                    },
                    "text": (
                        "The longhouse to the north: searched. The forge inside it, cold but yielded what it had. "
                        "To the east: the dense dead, and whatever woke among them, settled now. "
                        "The soldier against the shield-wall: gone, one way or another. "
                        "To the south the mound waits, and Gunnar with it. "
                        "There is nothing left to find here. Only the reckoning."
                    ),
                },
                {
                    "condition": {
                        "and": [{"flag": "found_forge"}, {"flag": "east_searched"}]
                    },
                    "text": (
                        "The longhouse to the north: searched, the forge cold but generous. "
                        "To the east: you have walked among the dense dead and returned. "
                        "A soldier still breathes against the shield-wall to the west — "
                        "or did, when you last looked. "
                        "To the south, the mound. You have not gone there yet."
                    ),
                },
                {
                    "condition": {"flag": "found_forge"},
                    "text": (
                        "The longhouse to the north: searched. The forge inside still breathes. "
                        "To the east, the dead lie thickest — you have not gone there yet. "
                        "Something moved among them, earlier. You remember that. "
                        "To the south, the mound."
                    ),
                },
                {
                    "condition": {"flag": "east_searched"},
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
            "label": "Search the longhouse ruins to the north.",
            "next": "longhouse_ruins",
            "effects": {"resolve": 2},
            "condition": {"not": {"flag": "found_forge"}},
        },
        {
            "label": "Go east — into the dense dead.",
            "next": "scavenge_east",
            "effects": {"brutality": 3},
            "condition": {"not": {"flag": "east_searched"}},
        },
        {
            "label": "Go to the soldier against the shield-wall.",
            "next": "soul_leif",
            "condition": {"not": {"flag": "leif_done"}},
        },
        {
            "label": "Go south — towards the mound.",
            "next": "the_mound",
            "condition": {"or": [{"flag": "found_forge"}, {"flag": "east_searched"}]},
        },
        {
            "label": "Return to the wider battlefield.",
            "next": "battlefield_open",
        },
    ],
}

SCENE_LEIF_FAREWELL = {
    "art": "leif",
    "beats": [
        {
            "type": "prose",
            "text": (
                "You move to leave. Leif's hand finds your wrist — "
                "not a grip, just a weight. "
                "He presses something into your palm."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"I found this the morning after the battle. '
                "Before the wound got bad enough that I stopped moving. "
                "It was on the mound — just sitting there, like it had been left. "
                "I do not know what it opens. "
                "But I kept it. "
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
            ),
        },
        {"type": "flag", "key": "leif_done"},
    ],
    "next": "leif_knife_offer",
}

SCENE_LEIF_AMBUSH = {
    "art": "leif",
    "beats": [
        {
            "type": "prose",
            "text": (
                "You turn away from Leif. "
                "Your mind is still on the conversation — on the name, on the weight of what he carried. "
                "You are not paying attention to the field."
            ),
        },
        {
            "type": "italic",
            "text": (
                "The sound reaches you before you understand it. "
                "Iron on iron. Close."
            ),
        },
        {
            "type": "prose",
            "text": (
                "One of the risen has been standing in the mud ten feet away, "
                "watching you with Leif, waiting. "
                "It has a shield — cracked along the rim but solid. "
                "It raises it now. "
                "It has been waiting for you to stop looking."
            ),
        },
    ],
    "next": "combat_shieldwall_leif",
}

SCENE_COMBAT_SHIELDWALL_LEIF = {
    "art": "combat_draugar",
    "next": "battlefield_open",
    "beats": [
        {
            "type": "combat",
            "enemy": "shieldwall_draugar",
            "variant": "veteran",
        },
        {"type": "stat", "changes": {"resolve": 3}},
    ],
}

SCENE_LEIF_KNIFE_OFFER = {
    "art": "leif",
    "beats": [
        {
            "type": "prose",
            "text": (
                "His knife is still on his belt. "
                "He has not offered it. He has not asked you to leave it."
            ),
        },
    ],
    "choices": [
        {
            "label": "Ask for the knife.",
            "next": "leif_knife_taken",
        },
        {
            "label": "Leave without it.",
            "next": "leif_ambush",
        },
    ],
}

SCENE_LEIF_KNIFE_TAKEN = {
    "art": "leif",
    "beats": [
        {
            "type": "prose",
            "text": "He nods. Once. As if he had been waiting to be asked.",
        },
        {
            "type": "item",
            "item": "Leif's knife",
            "action": "give",
        },
    ],
    "next": "leif_ambush",
}

SCENE_LEIF_MERCY_KILL = {
    "art": "leif",
    "beats": [
        {
            "type": "prose",
            "text": (
                "You stay. You do not speak. "
                "There is nothing useful to say and Leif is past needing it. "
                "His breathing slows in the way that breathing slows "
                "when there is no more reason to rush."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"Good," he says. Not to you, specifically. '
                "Just: good. Like a man setting down something he has carried a long way."
            ),
        },
        {
            "type": "prose",
            "text": (
                "When it is over you sit with it for a moment. "
                "Then you search him — not out of disrespect, "
                "but because the dead have no use for what they carry "
                "and you are not yet done with this battlefield."
            ),
        },
        {
            "type": "prose",
            "text": (
                "He has a knife, a pouch of echo dust, and a piece of birchbark "
                "with a name scratched into it. "
                "The name is yours. "
                "He carried it with him into the battle. "
                "You do not know yet whether that makes the weight lighter or heavier."
            ),
        },
        {"type": "item", "item": "Leif's knife", "action": "give"},
        {"type": "stat", "changes": {"echo_shards": 45}},
        {
            "type": "memory",
            "key": "leif_last_word",
            "label": "What Leif said at the end",
            "text": (
                "Good. That was all. "
                "One word, said the way you say a word "
                "when it is the last one and it has to be enough. "
                "It was enough."
            ),
        },
        {"type": "flag", "key": "leif_done"},
    ],
    "next": "leif_ambush",
}

SCENE_LEIF_DEFENSE = {
    "art": "leif",
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
            ),
        },
        {
            "type": "italic",
            "text": '"That\'s what I thought," says Leif. He does not say it unkindly.',
        },
    ],
    "next": "leif_gunnar_intro",
}

SCENE_LEIF_BATTLE_ACCOUNT = {
    "art": "leif",
    "beats": [
        {
            "type": "italic",
            "text": (
                '"It was a rout," Leif says. "Both sides. '
                "The Svear came from the east ridge at dawn. "
                "We had a scout there — should have seen them. "
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
            ),
        },
    ],
    "next": "leif_gives_name",
}

SCENE_LEIF_SURVIVORS = {
    "art": "leif",
    "beats": [
        {
            "type": "italic",
            "text": '"No one," Leif says simply. "Only you. And I won\'t be, soon."',
        },
        {
            "type": "prose",
            "text": ("He says it without drama. " "You find you appreciate that."),
        },
    ],
    "next": "leif_gives_name",
}

# ─────────────────────────────────────────────────────────────
#  LONGHOUSE RUINS
# ─────────────────────────────────────────────────────────────
SCENE_LONGHOUSE_RUINS = {
    "art": "longhouse",
    "header": {
        "title": "THE LONGHOUSE RUINS",
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
            ),
        },
        {
            "type": "prose",
            "text": (
                "Under a collapsed beam you find the forge. "
                "The coals are cold, but the tools remain. "
                "Someone built this forge to last. "
                "You recognise the craft in it — not because you remember where you learned, "
                "but because your hands do."
            ),
        },
        {
            "type": "flag",
            "key": "found_forge",
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
            ),
        },
        {
            "type": "heal",
            "amount": 100,
        },
        {
            "type": "memory",
            "key": "the_bone_cairn",
            "label": "The warmth of the first cairn",
            "text": (
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
            "label": "Rest at the cairn. You have time.",
            "next": "cairn_rest",
            "effects": {"resolve": 8},
            "flags": {"rested_at_cairn": True},
        },
        {
            "label": "Search the forge for usable materials.",
            "next": "forge_search",
            "condition": {"not": {"flag": "forge_searched"}},
        },
        {
            "label": "Sharpen your axe with the whetstone.",
            "next": "forge_sharpen",
            "condition": {
                "and": [
                    {"has_item": "rusted axe"},
                    {"has_item": "whetstone"},
                    {"not": {"flag": "axe_sharpened"}},
                ]
            },
        },
        {
            "label": "Sit with the dying embers a moment.",
            "next": "longhouse_embers",
            "condition": {"not": {"flag": "embers_remembered"}},
        },
        {
            "label": "Return to the battlefield.",
            "next": "battlefield_open",
        },
    ],
}

SCENE_LONGHOUSE_EMBERS = {
    "art": "longhouse",
    "beats": [
        {
            "type": "prose",
            "text": (
                "You crouch by what remains of the fire — "
                "not much, a few coals still holding orange beneath grey ash. "
                "You hold your hands out. "
                "The warmth is faint, but it is real."
            ),
        },
        {
            "type": "italic",
            "text": (
                "And then it finds you: a hearth. "
                "A specific hearth, in a specific hall, "
                "on a night when the wind was loud outside "
                "and the fire was louder inside. "
                "Someone sitting close enough that your shoulders touched. "
                "You do not remember who. "
                "You remember that you did not want to move."
            ),
        },
        {
            "type": "memory",
            "key": "the_hearth",
            "label": "A hearth in winter",
            "text": (
                "A hall. A fire. Wind loud outside and warmth louder inside. "
                "Someone sitting close enough that your shoulders touched. "
                "You do not remember who. "
                "You remember that you did not want to move."
            ),
        },
        {"type": "flag", "key": "embers_remembered"},
    ],
    "next": "longhouse_ruins",
}

SCENE_CAIRN_REST = {
    "art": "cairn",
    "beats": [
        {
            "type": "prose",
            "text": (
                "You sit with your back against the cairn. "
                "The warmth is steady — not warm like fire, "
                "but warm like something that has been burning so long "
                "it has forgotten how to stop. "
                "You close your eyes and let the memory try to find you."
            ),
        },
        {
            "type": "memory",
            "key": "the_feast",
            "label": "A feast in the longhouse — before",
            "text": (
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
            ),
        },
        {
            "type": "prose",
            "text": (
                "You open your eyes. "
                "The fog is the same. The battlefield is the same. "
                "But something has shifted — "
                "not in the world, but in the distance between you and what you lost. "
                "It is smaller than it was."
            ),
        },
        {"type": "heal", "amount": 30},
    ],
    "next": "battlefield_open",
}

SCENE_FORGE_SEARCH = {
    "art": "longhouse",
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
            ),
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
            ),
        },
        {"type": "item", "item": "iron scraps", "action": "give"},
        {"type": "item", "item": "whetstone", "action": "give"},
        {"type": "stat", "changes": {"echo_shards": 80}},
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
            ),
        },
        {
            "type": "memory",
            "key": "the_medallion",
            "label": "A clan medallion, familiar and nameless",
            "text": (
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
    "next": "longhouse_ruins",
}

SCENE_FORGE_SHARPEN = {
    "art": "longhouse",
    "beats": [
        {
            "type": "prose",
            "text": (
                "You lock the rusted axe in the vice and take up the whetstone. "
                "The sound it makes against the edge is the sound of patience — "
                "slow strokes, angle held constant, "
                "the same pressure at the heel as at the tip. "
                "Your hands know this. "
                "They do not need you to remember why."
            ),
        },
        {
            "type": "italic",
            "text": (
                "Stone on iron. The smell of metal going warm. "
                "The specific satisfaction of something made right."
            ),
        },
        {
            "type": "prose",
            "text": (
                "When you test the edge against your thumb it catches cleanly. "
                "Not a warrior's blade — not yet — "
                "but a tool that will hold what you ask of it. "
                "You wipe the iron filings from the flat and feel "
                "something settle in your chest. "
                "The rust is gone. The edge is yours."
            ),
        },
        {"type": "item", "item": "rusted axe", "action": "take"},
        {"type": "item", "item": "sharpened axe", "action": "give"},
        {"type": "flag", "key": "axe_sharpened"},
        {
            "type": "memory",
            "key": "axe_sharpened",
            "label": "The Whetstone",
            "text": (
                "Stone on iron. Slow strokes, constant angle. "
                "Your hands knew the work before your mind did. "
                "You do not remember who taught you — "
                "only that someone did, once, and that it mattered."
            ),
        },
    ],
    "next": "longhouse_ruins",
}

# ─────────────────────────────────────────────────────────────
#  SCAVENGE EAST
# ─────────────────────────────────────────────────────────────
SCENE_SCAVENGE_EAST = {
    "art": "scavenge",
    "header": {
        "title": "THE DENSE DEAD",
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
            ),
        },
        {
            "type": "prose",
            "text": (
                "You move through them carefully. Searching. "
                "You tell yourself you are looking for supplies. "
                "This is partly true."
            ),
        },
        {"type": "stat", "changes": {"echo_shards": 120}},
        {"type": "item", "item": "iron scraps", "action": "give"},
        {
            "type": "prose",
            "text": (
                "Then one of them moves. "
                "Not all at once — a hand first, then a shoulder, "
                "then the slow terrible process of something that has been dead "
                "deciding that it has unfinished business."
            ),
        },
        {"type": "pause", "msg": "  [ you are not alone ]"},
    ],
    "choices": [
        {
            "label": "Stand your ground. Face it.",
            "next": "combat_draugar_east",
            "effects": {"honour": 5, "brutality": 3},
        },
        {
            "label": "Back away slowly. You choose your battles.",
            "next": "battlefield_open",
            "effects": {"honour": -3, "resolve": 3},
            "narration": (
                "You back into the fog. "
                "The thing follows you with its eyes — "
                "but eyes are the only thing it can move quickly. "
                "You are gone before the rest of it is upright."
            ),
        },
        {
            "label": "Strike first. Before it is fully awake.",
            "next": "combat_draugar_east",
            "effects": {"brutality": 8, "honour": -5},
            "narration": "You do not give it the chance to stand.",
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  COMBAT SCENES
# ─────────────────────────────────────────────────────────────
SCENE_COMBAT_DRAUGAR_EAST = {
    "art": "combat_draugar",
    "next": "scavenge_east_after",
    "beats": [
        {
            "type": "combat",
            "enemy": "draugar_weak",
            "flag": "defeated_draugar_east",
        },
        {"type": "stat", "changes": {"brutality": 3}},
    ],
    "choices": [
        {
            "label": "Search the bodies more carefully.",
            "next": "scavenge_east_after",
        },
        {
            "label": "Return to the wider battlefield.",
            "next": "battlefield_open",
        },
    ],
}

SCENE_SCAVENGE_EAST_AFTER = {
    "art": "scavenge",
    "beats": [
        {
            "type": "prose",
            "text": (
                "The battlefield settles again. "
                "You stand in it, breathing. "
                "The quiet after violence is a specific kind of quiet. "
                "You recognise it."
            ),
        },
        {
            "type": "prose",
            "text": (
                "Now that the immediate threat is settled, you search properly. "
                "The dead here carry more than the others — "
                "this was where the officers fell."
            ),
        },
        {"type": "stat", "changes": {"echo_shards": 180}},
        {"type": "item", "item": "reinforced vambrace", "action": "give"},
        {
            "type": "memory",
            "key": "the_officers",
            "label": "The rank of those who fell last",
            "text": (
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
    "art": "mound",
    "header": {
        "title": "THE MOUND OF OATHBREAKERS",
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
            ),
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": {"memory": "the_broken_oath"},
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
            ],
        },
        {
            "type": "prose",
            "text": (
                "He is waiting for you. "
                "He has been waiting for you since before you woke."
            ),
        },
        {
            "type": "italic",
            "text": '"I knew you would come here," says Gunnar. "This is where oathbreakers end up."',
        },
        {"type": "pause"},
        {
            "type": "memory",
            "key": "the_death",
            "label": "The memory of dying",
            "text": (
                "The mud. The screaming, already fading. "
                "The axe — not this one, a different one — coming from above. "
                "And then: nothing. "
                "That is all you have. The rest is still fog. "
                "But the nothing at the end — that part is very clear."
            ),
        },
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
            ),
        },
    ],
    "choices": [
        {
            "label": '"I am not here to fight you."',
            "next": "gunnar_dialogue_peace",
            "effects": {"honour": 5},
        },
        {
            "label": '"Then this is where I end it."',
            "next": "gunnar_dialogue_challenge",
            "effects": {"brutality": 5, "resolve": 5},
        },
        {
            "label": '"Tell me what I did."',
            "next": "gunnar_dialogue_truth",
            "condition": {"memory": "the_broken_oath"},
        },
    ],
}

SCENE_GUNNAR_DIALOGUE_PEACE = {
    "art": "gunnar",
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
    "art": "gunnar",
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
            ),
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
            ),
        },
        {"type": "stat", "changes": {"resolve": 5}},
    ],
    "next": "combat_gunnar",
}

SCENE_GUNNAR_DIALOGUE_TRUTH = {
    "art": "gunnar",
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
            "key": "the_truth",
            "label": "What Gunnar remembers",
            "text": (
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
    "art": "gunnar",
    "next": "act1_end",
    "beats": [
        {
            "type": "combat",
            "enemy": "gunnar",
            "flag": "gunnar_defeated",
        },
    ],
    "choices": [
        {
            "label": "Go to him. Hear what he has to say.",
            "next": "act1_end",
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  ZONE 1 END
# ─────────────────────────────────────────────────────────────
SCENE_ACT1_END = {
    "art": "mound",
    "header": {
        "title": "SILENCE FALLS",
        "subtitle": "The Battlefield of Silence — cleared",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "He is on one knee. Not defeated — you do not think he can be defeated, "
                "not truly — but spent. The axe is in the mud. "
                "His hands are open."
            ),
        },
        {
            "type": "prose",
            "text": (
                "You look at the axe. It is not a trophy. "
                "You do not pick it up as a trophy. "
                "But you pick it up."
            ),
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
                "I watched every one of them stop moving. "
                'I did not stop."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"I think I am here because of you. '
                "I think I was waiting. "
                'I do not know what I am now that the waiting is done."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "He reaches into his coat and holds something out. "
                "An iron key, old and heavy, marked with a rune you almost recognise."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"Take it. It opens something to the south — '
                "I found it on the third day, when I was still looking for a reason. "
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
            "key": "the_first_victory",
            "label": "What it felt like to defeat your commander",
            "text": (
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
            ),
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
            ),
        },
    ],
    "choices": [
        {
            "label": "Walk south. Into whatever comes next.",
            "next": "act_2_intro",
            "effects": {"resolve": 10},
        },
        {
            "label": "Rest first. The cairn. One more night.",
            "next": "final_rest",
            "effects": {"resolve": 5, "honour": 5},
        },
    ],
}

SCENE_FINAL_REST = {
    "art": "cairn",
    "header": {
        "title": "THE BONE CAIRN",
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
            ),
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
            ),
        },
        {
            "type": "italic",
            "text": (
                "The cairn hums very quietly. "
                "Or perhaps that is you. "
                "The distinction has become less important."
            ),
        },
        {
            "type": "prose",
            "text": (
                "When you open your eyes the fog to the south is lighter. "
                "Not gone — never gone — but thinner. "
                "The key is warm in your hand. "
                "It is time."
            ),
        },
        {"type": "stat", "changes": {"resolve": 8, "honour": 5}},
        {"type": "heal", "amount": 100},
    ],
    "next": "act_2_intro",
}

SCENE_ACT_2_INTRO = {
    "art": "act_break",
    "header": {
        "title": "ACT II",
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
            ),
        },
        {
            "type": "prose",
            "text": (
                "You walk for what might be an hour or might be a day. "
                "You do not tire the way you used to tire. "
                "Your body remembers exhaustion as a concept "
                "but has stopped practising it. "
                "This should be more disturbing than it is."
            ),
        },
        {
            "type": "italic",
            "text": (
                "Somewhere behind you, the battlefield. "
                "Ten thousand dead who stayed dead. "
                "One who didn't. "
                "You."
            ),
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
            ),
        },
        {
            "type": "italic",
            "text": "The fog does not lift. It never lifts. But you are still walking in it.",
        },
    ],
    "choices": [
        {
            "label": "Continue south. The key grows warmer.",
            "next": "fog_road",
        },
        {
            "label": "Return to the battlefield (restart Act 1).",
            "next": "__restart__",
        },
    ],
}

# ═════════════════════════════════════════════════════════════
#  ACT II — THE STIRRING BENEATH
# ═════════════════════════════════════════════════════════════


SCENES = {
    "name_entry": SCENE_NAME_ENTRY,
    "awakening": SCENE_AWAKENING,
    "find_weapon": SCENE_FIND_WEAPON,
    "battlefield_open": SCENE_BATTLEFIELD_OPEN,
    "battlefield_look_around": SCENE_BATTLEFIELD_LOOK_AROUND,
    "soul_leif": SCENE_SOUL_LEIF,
    "leif_gives_name": SCENE_LEIF_GIVES_NAME,
    "leif_the_oath": SCENE_LEIF_THE_OATH,
    "leif_gunnar_intro": SCENE_LEIF_GUNNAR_INTRO,
    "leif_farewell": SCENE_LEIF_FAREWELL,
    "leif_ambush": SCENE_LEIF_AMBUSH,
    "combat_shieldwall_leif": SCENE_COMBAT_SHIELDWALL_LEIF,
    "leif_knife_offer": SCENE_LEIF_KNIFE_OFFER,
    "leif_knife_taken": SCENE_LEIF_KNIFE_TAKEN,
    "leif_mercy_kill": SCENE_LEIF_MERCY_KILL,
    "leif_defense": SCENE_LEIF_DEFENSE,
    "leif_battle_account": SCENE_LEIF_BATTLE_ACCOUNT,
    "leif_survivors": SCENE_LEIF_SURVIVORS,
    "longhouse_ruins": SCENE_LONGHOUSE_RUINS,
    "longhouse_embers": SCENE_LONGHOUSE_EMBERS,
    "cairn_rest": SCENE_CAIRN_REST,
    "forge_search": SCENE_FORGE_SEARCH,
    "forge_sharpen": SCENE_FORGE_SHARPEN,
    "scavenge_east": SCENE_SCAVENGE_EAST,
    "combat_draugar_east": SCENE_COMBAT_DRAUGAR_EAST,
    "scavenge_east_after": SCENE_SCAVENGE_EAST_AFTER,
    "the_mound": SCENE_THE_MOUND,
    "gunnar_dialogue_peace": SCENE_GUNNAR_DIALOGUE_PEACE,
    "gunnar_dialogue_challenge": SCENE_GUNNAR_DIALOGUE_CHALLENGE,
    "gunnar_dialogue_truth": SCENE_GUNNAR_DIALOGUE_TRUTH,
    "combat_gunnar": SCENE_COMBAT_GUNNAR,
    "act1_end": SCENE_ACT1_END,
    "final_rest": SCENE_FINAL_REST,
    "act_2_intro": SCENE_ACT_2_INTRO,
}
