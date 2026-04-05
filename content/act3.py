# ============================================================
#  content/act3.py
#  Act III — The Silence Beneath
#  Opens with the Tyr temple encounter.
# ============================================================

# ─────────────────────────────────────────────────────────────
#  TYR'S TEMPLE
# ─────────────────────────────────────────────────────────────

SCENE_TYR_TEMPLE_APPROACH = {
    "art": "tyr_temple",
    "beats": [
        {
            "type": "prose",
            "text": (
                "The fog does not thin here — it simply stops. "
                "As if something older than the fog drew a line "
                "and the fog respected it."
            ),
        },
        {
            "type": "prose",
            "text": (
                "The temple is small. Smaller than you expected for a god. "
                "Timber, darkened with age, listing slightly to the east "
                "as if it has been leaning into the same wind for a very long time. "
                "No carvings on the door. No runes. "
                "Just wood, and the grain of it, and the years."
            ),
        },
        {
            "type": "italic",
            "text": "The key is cold again. It has been cold since the fog stopped.",
        },
        {
            "type": "prose",
            "text": (
                "There is a light inside. Not fire — something steadier than fire. "
                "The kind of light that does not need tending."
            ),
        },
    ],
    "choices": [
        {
            "label": "Enter.",
            "next": "tyr_temple_interior",
        },
        {
            "label": "Leave something at the threshold first.",
            "next": "tyr_temple_offering",
        },
        {
            "label": "Wait outside. Not yet.",
            "next": "tyr_temple_wait",
            "effects": {"resolve": -3},
        },
    ],
}

SCENE_TYR_TEMPLE_OFFERING = {
    "art": "tyr_temple",
    "beats": [
        {
            "type": "prose",
            "text": (
                "There is a flat stone at the base of the door. "
                "Worn smooth at the centre — many hands, or one pair of hands "
                "over a very long time. "
                "It has been used for this before."
            ),
        },
    ],
    "choices": [
        {
            "label": "Leave Gunnar's Axe.",
            "next": "tyr_temple_offered_axe",
            "condition": {"has_item": "Gunnar's Axe"},
            "flags": {"offered_gunnars_axe": True},
            "effects": {"honour": 10},
        },
        {
            "label": "Leave the bear pelt.",
            "next": "tyr_temple_offered_bear_pelt",
            "condition": {"has_item": "bear pelt"},
            "flags": {"offered_pelt": True},
            "effects": {"honour": 5, "brutality": -5},
        },
        {
            "label": "Leave the wolf pelt.",
            "next": "tyr_temple_offered_wolf_pelt",
            "condition": {
                "and": [
                    {"has_item": "wolf pelt"},
                    {"not": {"has_item": "bear pelt"}},
                ]
            },
            "flags": {"offered_pelt": True},
            "effects": {"honour": 3},
        },
        {
            "label": "You have nothing worth leaving. Enter anyway.",
            "next": "tyr_temple_interior",
        },
    ],
}

SCENE_TYR_TEMPLE_OFFERED_AXE = {
    "art": "tyr_temple",
    "beats": [
        {"type": "item", "action": "take", "item": "Gunnar's Axe"},
        {
            "type": "prose",
            "text": (
                "You set the axe on the stone. "
                "It is heavier than it should be, leaving your hand. "
                "Or perhaps you have been holding it tightly for a long time "
                "without noticing."
            ),
        },
        {
            "type": "italic",
            "text": "It was never yours. You knew that. You carried it anyway.",
        },
        {
            "type": "prose",
            "text": "You straighten. The door is in front of you.",
        },
    ],
    "choices": [
        {
            "label": "Enter.",
            "next": "tyr_temple_interior",
        },
    ],
}

SCENE_TYR_TEMPLE_OFFERED_BEAR_PELT = {
    "art": "tyr_temple",
    "beats": [
        {"type": "item", "action": "take", "item": "bear pelt"},
        {
            "type": "prose",
            "text": (
                "You fold the pelt and set it on the stone. "
                "It is warm — it has always been warm. "
                "You do not know if what you are leaving behind "
                "is the animal or what wearing it made you."
            ),
        },
        {
            "type": "prose",
            "text": "You straighten. The door is in front of you.",
        },
    ],
    "choices": [
        {
            "label": "Enter.",
            "next": "tyr_temple_interior",
        },
    ],
}

SCENE_TYR_TEMPLE_OFFERED_WOLF_PELT = {
    "art": "tyr_temple",
    "beats": [
        {"type": "item", "action": "take", "item": "wolf pelt"},
        {
            "type": "prose",
            "text": (
                "You fold the pelt and set it on the stone. "
                "It is warm — it has always been warm. "
                "You do not know if what you are leaving behind "
                "is the animal or what wearing it made you."
            ),
        },
        {
            "type": "prose",
            "text": "You straighten. The door is in front of you.",
        },
    ],
    "choices": [
        {
            "label": "Enter.",
            "next": "tyr_temple_interior",
        },
    ],
}

SCENE_TYR_TEMPLE_WAIT = {
    "art": "tyr_temple",
    "beats": [
        {
            "type": "prose",
            "text": (
                "You stand outside for a long time. "
                "The light inside does not change. "
                "Whatever is in there is not impatient."
            ),
        },
        {
            "type": "italic",
            "text": (
                "A voice comes through the wood, unhurried: "
                '"Take the time you need. I have had longer waits than this."'
            ),
        },
    ],
    "choices": [
        {
            "label": "Enter.",
            "next": "tyr_temple_interior",
        },
    ],
}

SCENE_TYR_TEMPLE_INTERIOR = {
    "art": "tyr",
    "beats": [
        {
            "type": "prose",
            "text": (
                "He is sitting on the floor with his back against the far wall. "
                "Not on a throne, not at an altar — on the floor, "
                "like a man who has been sitting there long enough "
                "that standing no longer seems worth the effort."
            ),
        },
        {
            "type": "prose",
            "text": (
                "He is large in the way that old things are large — "
                "not with bulk but with presence. "
                "His right arm ends at the wrist. "
                "He does not hide it."
            ),
        },
        {
            "type": "italic",
            "text": '"Odin\'s work again," he says. "I can always tell."',
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": {"flag": "offered_gunnars_axe"},
                    "text": (
                        "His eyes move to your empty hand. "
                        "He knows what was there. "
                        "He does not say anything about it. "
                        "He does not need to."
                    ),
                },
                {
                    "condition": {"flag": "offered_pelt"},
                    "text": (
                        "He glances toward the door — toward what you left outside. "
                        "A small acknowledgement. Nothing more."
                    ),
                },
            ],
        },
        {"type": "pause"},
        {
            "type": "italic",
            "text": (
                '"Sit down. '
                "I am not going to shout the charges at you. "
                'I have done that enough times to know it helps no one."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "You sit. "
                "The light is coming from a shallow bowl on the ground between you. "
                "No oil, no wick. It is simply burning."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"You left your position," he says. '
                '"That is what it looks like from outside. '
                'That is what the oath says. That is what I am here to weigh."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"But I have been watching Odin work for a long time. '
                "Long enough to know what his hand looks like "
                "when it moves through a man's life.\""
            ),
        },
        {
            "type": "prose",
            "text": "He looks at you without accusation. That is almost worse.",
        },
        {
            "type": "italic",
            "text": '"Tell me what you remember. Not what you did. What you remember."',
        },
    ],
    "choices": [
        {
            "label": '"I remember leaving. I do not remember why."',
            "next": "tyr_dialogue_no_words",
            "effects": {"honour": 5},
        },
        {
            "label": '"I had a reason. I cannot explain it."',
            "next": "tyr_dialogue_no_words",
            "effects": {"resolve": 5},
        },
        {
            "label": '"I remember Gunnar\'s face when I came back and he was already dead."',
            "next": "tyr_dialogue_grief",
            "effects": {"mercy": 5},
        },
    ],
}

SCENE_TYR_DIALOGUE_NO_WORDS = {
    "art": "tyr",
    "beats": [
        {
            "type": "italic",
            "text": "He nods slowly. As if this is the answer he expected.",
        },
        {
            "type": "italic",
            "text": (
                '"That is how he works. '
                "No words. Just certainty. "
                "You know, and you cannot say how you know, "
                'and you cannot unknow it."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "He lifts his arm — the one that ends at the wrist — "
                "and looks at it for a moment."
            ),
        },
        {
            "type": "italic",
            "text": (
                "\"I held my hand in the wolf's mouth because it was necessary. "
                "Everyone agreed it was necessary. "
                "The wolf did not agree, but the wolf was not asked. "
                'I was not asked either, in the end. I simply knew."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"The difference between us," he says quietly, '
                '"is that I knew what I was losing. '
                'I think you did not."'
            ),
        },
    ],
    "next": "tyr_judgement",
}

SCENE_TYR_DIALOGUE_GRIEF = {
    "art": "tyr",
    "beats": [
        {
            "type": "prose",
            "text": "He is quiet for a long time.",
        },
        {
            "type": "italic",
            "text": (
                '"That is not an answer to my question," he says. '
                '"But it is an honest one."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"Grief is not guilt. '
                "They feel the same from the inside, "
                'but they are not the same thing."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "He picks up a small stone from beside the bowl "
                "and turns it over in his remaining hand. "
                "Sets it down."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"You carry both. '
                "That is Odin's real gift — "
                "he does not give you a burden you can put down. "
                'He gives you one that feels like it belongs to you."'
            ),
        },
    ],
    "next": "tyr_judgement",
}

SCENE_TYR_JUDGEMENT = {
    "art": "tyr",
    "beats": [
        {
            "type": "prose",
            "text": (
                "He stands. Slowly, with the particular care of something "
                "that has been sitting too long. "
                "He is taller than you remembered — taller than the room "
                "seems to allow, though the ceiling does not stop him."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"I cannot clear you," he says. '
                '"The oath was spoken. The oath was not kept. '
                "That is the law and I am the law "
                'and I do not get to prefer one outcome over another."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"But I can tell you this: '
                "Odin will answer for what he does with men. "
                "Not today. Not to me. "
                'But the reckoning comes for all of us, in the end."'
            ),
        },
        {
            "type": "memory",
            "key": "tyr_witness",
            "label": "What the law god said",
            "text": (
                "He did not forgive you. "
                "He did not condemn you either — not entirely. "
                "He simply named what happened and stood beside the naming of it. "
                "That is, you think, the most honest thing anyone has done "
                "since you woke."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"There is something further in. '
                "Past the temple, past where the light reaches. "
                "I have been watching it pull at you since you sat down. "
                'Go. Whatever it is, it has been waiting longer than I have."'
            ),
        },
    ],
    "choices": [
        {
            "label": '"Thank you."',
            "next": "tyr_farewell",
            "effects": {"honour": 5},
        },
        {
            "label": "Say nothing. Turn and go.",
            "next": "tyr_farewell",
            "effects": {"resolve": 5},
        },
    ],
}

SCENE_TYR_FAREWELL = {
    "art": "tyr_temple",
    "beats": [
        {
            "type": "prose",
            "text": (
                "Outside, the fog has pulled back a little further. "
                "Not much. Enough."
            ),
        },
        {
            "type": "prose",
            "text": (
                "Behind you the temple light is still burning. "
                "You do not look back at it. "
                "You have the sense that if you did, "
                "he would still be sitting there, "
                "watching the door with the patience "
                "of something that will outlast the watching."
            ),
        },
        {
            "type": "italic",
            "text": "Further in. The key knows the way.",
        },
    ],
    "choices": [
        {
            "label": "Follow the key. Into the dark.",
            "next": "crossroads_memory",
            "effects": {"resolve": 5},
        },
    ],
}

SCENE_CROSSROADS_MEMORY = {
    "art": "act_break",
    "beats": [
        {
            "type": "italic",
            "text": "Coming soon.",
        },
    ],
    "choices": [
        {
            "label": "Return to the beginning (restart).",
            "next": "__restart__",
        },
    ],
}

# ─────────────────────────────────────────────────────────────

SCENES = {
    "tyr_temple_approach": SCENE_TYR_TEMPLE_APPROACH,
    "tyr_temple_wait": SCENE_TYR_TEMPLE_WAIT,
    "tyr_temple_offering": SCENE_TYR_TEMPLE_OFFERING,
    "tyr_temple_offered_axe": SCENE_TYR_TEMPLE_OFFERED_AXE,
    "tyr_temple_offered_bear_pelt": SCENE_TYR_TEMPLE_OFFERED_BEAR_PELT,
    "tyr_temple_offered_wolf_pelt": SCENE_TYR_TEMPLE_OFFERED_WOLF_PELT,
    "tyr_temple_interior": SCENE_TYR_TEMPLE_INTERIOR,
    "tyr_dialogue_no_words": SCENE_TYR_DIALOGUE_NO_WORDS,
    "tyr_dialogue_grief": SCENE_TYR_DIALOGUE_GRIEF,
    "tyr_judgement": SCENE_TYR_JUDGEMENT,
    "tyr_farewell": SCENE_TYR_FAREWELL,
    "crossroads_memory": SCENE_CROSSROADS_MEMORY,
}
