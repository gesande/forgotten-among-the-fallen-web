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
    "art": "crossroads",
    "cinematic": True,
    "header": {
        "title": "THE CROSSROADS",
        "subtitle": "you have been here before",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "Four paths. "
                "The one behind you — the temple, the fog, the way you came. "
                "Three others, leading into grey that could be anything. "
                "The fog does not move here. "
                "It stands the way old things stand: without effort, without intention, "
                "simply present."
            ),
        },
        {
            "type": "prose",
            "text": (
                "You have stopped walking without deciding to. "
                "The key is in your hand — it has been in your hand since the temple, "
                "since before the temple. "
                "Since Gunnar pressed it into yours and fell."
            ),
        },
        {
            "type": "prose",
            "text": (
                "It begins to warm. "
                "Not the warmth of iron held too long. "
                "The warmth of something waking up."
            ),
        },
        {
            "type": "italic",
            "text": (
                "The rune ᛗ catches what little light there is. "
                "Mannaz. You stare at it and the crossroads tilts — "
                "not the one you are standing in but another one, "
                "older, real, mud underfoot and torches and the smell of cold earth —"
            ),
        },
        {
            "type": "italic",
            "text": (
                "Gunnar is there. Younger. You are younger. "
                "He is saying something. You cannot hear the words. "
                "You watch your own hands in the memory — "
                "they reach up and remove something from around your neck. "
                "Small. Iron. Carved. "
                "Something you have worn since before you could name it."
            ),
        },
        {
            "type": "italic",
            "text": (
                "You press it into his hand. You close his fingers around it. "
                "You say something. You can almost hear it. "
                "Four words. Five."
            ),
        },
        {
            "type": "italic",
            "text": "If I break this — take it. Take my name with it.",
        },
        {
            "type": "prose",
            "text": "And then it is gone.",
        },
        {
            "type": "prose",
            "text": (
                "You are standing at the crossroads. "
                "The key is cold. "
                "Not cold the way iron goes cold in fog — "
                "cold the way something goes "
                "when it has given what it was made to give."
            ),
        },
        {
            "type": "prose",
            "text": (
                "Your naming-rune. "
                "Iron, small, worn at your throat since your father carved it "
                "before you could speak. "
                "The name that was yours before everything else was. "
                "You gave it as surety. You gave it as proof."
            ),
        },
        {
            "type": "prose",
            "text": (
                "You do not remember what happened next. "
                "The memory ends at the closing of his hand."
            ),
        },
        {
            "type": "prose",
            "text": (
                "The fog shifts. Not much. "
                "Something has changed in it — "
                "the way a room changes when someone enters "
                "who was already there."
            ),
        },
    ],
    "next": "odin_appears",
}

# ─────────────────────────────────────────────────────────────
#  ODIN — placeholder
# ─────────────────────────────────────────────────────────────

SCENE_ODIN_APPEARS = {
    "art": "odin",
    "cinematic": True,
    "beats": [
        {
            "type": "prose",
            "text": (
                "A raven lands at the centre of the crossroads. "
                "Coal-black, large, entirely still. "
                "It does not look at you — "
                "it looks at the place where the four paths meet, "
                "as if it is reading something written there."
            ),
        },
        {
            "type": "prose",
            "text": (
                "At the edge of the fog — the left path, the one you have not "
                "looked at closely — something stands. "
                "Grey. Low. Patient. "
                "You know the shape. "
                "You have seen it before."
            ),
        },
        {
            "type": "italic",
            "text": (
                "The wolf in the mist. The raven at the crossroads. "
                "You have been here before too — "
                "not this place, but this moment."
            ),
        },
        {
            "type": "prose",
            "text": ("You look back at the raven. " "The raven is not there."),
        },
        {
            "type": "prose",
            "text": (
                "An old man stands at the centre of the crossroads. "
                "One eye. Wide-brimmed hat. A staff worn smooth by more years "
                "than the wood should have survived. "
                "Plain travelling clothes — the clothes of a man who goes "
                "everywhere and needs no one to know it."
            ),
        },
        {
            "type": "prose",
            "text": (
                "He was already there. "
                "Before the raven. Before the wolf. "
                "Before you arrived at this crossroads eleven years ago "
                "and made the choice that brought you here."
            ),
        },
        {
            "type": "italic",
            "text": "He does not speak first. He is waiting for you to understand that he doesn't have to.",
        },
    ],
    "choices": [
        {
            "label": '"You planned this." — all of it.',
            "next": "odin_confrontation",
            "effects": {"honour": 5},
        },
        {
            "label": "Say nothing. Wait.",
            "next": "odin_confrontation",
            "effects": {"resolve": 5},
        },
        {
            "label": '"I remember you." — the wolf. The crossroads.',
            "next": "odin_confrontation",
            "effects": {"mercy": 5},
            "condition": {"or": [{"flag": "wolf_spared"}, {"flag": "wolf_killed"}]},
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  ODIN — CONFRONTATION
# ─────────────────────────────────────────────────────────────

SCENE_ODIN_CONFRONTATION = {
    "art": "odin",
    "cinematic": True,
    "beats": [
        {
            "type": "italic",
            "text": '"Not all of it," he says. "Enough of it."',
        },
        {
            "type": "prose",
            "text": (
                "He does not move toward you. He does not need to. "
                "There is a quality to his stillness that is not patience — "
                "something older than patience, that came before the word."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"I have been moving men through that valley '
                "for longer than your bloodline has had a name. "
                "You are not the first who left a post. "
                'You are not the first who did not understand why."'
            ),
        },
        {
            "type": "prose",
            "text": "His one eye finds you. It is not unkind. That is almost harder.",
        },
        {
            "type": "italic",
            "text": (
                '"I did not give you a reason. '
                "Reasons can be refused. "
                "What I gave you was a pull — "
                "the pull that takes men out of warm beds onto ships "
                "before dawn and they cannot tell you afterward what moved them. "
                'That is my oldest work."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "You are still holding the key. "
                "Your hand has closed around it. "
                "He is looking at it."
            ),
        },
    ],
    "choices": [
        {
            "label": '"And Gunnar? Was he oldest work too?"',
            "next": "odin_gunnar",
            "effects": {"mercy": 5},
        },
        {
            "label": '"What did you need the oath broken for?"',
            "next": "odin_the_reason",
            "effects": {"resolve": 5},
        },
        {
            "label": '"You have no right to move men without their knowing."',
            "next": "odin_the_reason",
            "effects": {"honour": 5},
        },
    ],
}

SCENE_ODIN_GUNNAR = {
    "art": "odin",
    "cinematic": True,
    "beats": [
        {
            "type": "prose",
            "text": (
                "He is quiet. Not considering — he does not need to consider. "
                "Deciding how much to give you."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"Gunnar Ironside." '
                "He says the name the way you say the name of a place "
                "you have walked through once and will not again."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"He was not meant to die on that day. '
                "He was meant to die three days later, "
                "in a different valley, "
                "with no one there who knew him well enough to mourn correctly. "
                "I changed the manner. I cannot tell you I changed the outcome. "
                'He was a fixed point. Not every man is."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "You do not know if this is supposed to comfort you. "
                "You do not think he is trying to comfort you. "
                "You think he is simply telling you what is true, "
                "the way he tells all things: without inflection, without apology."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"What changed," he says, '
                '"is that you were there. '
                "When a fixed point ends, someone should be there who knew. "
                "That is not comfort. "
                'That is just — what should happen, when the world is working correctly."'
            ),
        },
    ],
    "next": "odin_the_naming",
}

SCENE_ODIN_THE_REASON = {
    "art": "odin",
    "cinematic": True,
    "beats": [
        {
            "type": "italic",
            "text": (
                '"The oath you swore was a lock," he says. '
                '"I needed the lock opened."'
            ),
        },
        {
            "type": "prose",
            "text": "He does not say what was locked. You notice that he does not.",
        },
        {
            "type": "italic",
            "text": (
                '"You are angry because I moved you without asking. '
                "I understand the anger. I have earned it before and I will earn it again. "
                "But the men I ask — they carry the weight of the asking afterward. "
                "They spend the rest of their lives wondering if they chose. "
                "The men I move — they spend it wondering why. "
                'One of those lives is longer."'
            ),
        },
        {
            "type": "prose",
            "text": "You do not say anything. He does not seem to expect you to.",
        },
        {
            "type": "italic",
            "text": (
                '"You are here," he says, '
                '"because you broke something you did not know you were breaking for me. '
                "That is the cleanest kind of breaking. "
                'No intention. No guilt that was ever really yours."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "That last part lands wrong. "
                "You have carried the guilt this far "
                "and it does not feel like something you are ready to set down "
                "just because he says it was never yours."
            ),
        },
    ],
    "next": "odin_the_naming",
}

SCENE_ODIN_THE_NAMING = {
    "art": "odin",
    "cinematic": True,
    "beats": [
        {
            "type": "prose",
            "text": (
                "He takes a step toward you. "
                "Not threatening — measured. "
                "He stops when he can see the key clearly."
            ),
        },
        {
            "type": "italic",
            "text": '"Your naming-rune," he says. "You know that now."',
        },
        {
            "type": "prose",
            "text": "You know that now.",
        },
        {
            "type": "italic",
            "text": (
                '"He kept it. Eleven years. '
                "Through campaigns and winter quarters and the particular erosion "
                "of long service that eats away at everything a man carries "
                "that is not strictly necessary. "
                'He kept it."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "You have not thought about that until now. "
                "What it means to carry something for eleven years "
                "when the person who gave it to you was not there. "
                "When the person who gave it to you had broken the oath it was surety for."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"A man who keeps something when he has every reason to discard it — '
                "that is its own kind of faithfulness. "
                "He did not forgive what you did. "
                "He did not stop keeping it either. "
                'Both things were true. He managed both."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "He is still looking at the key. "
                "Or rather — he is looking at what the key is, "
                "underneath what it has become."
            ),
        },
        {
            "type": "italic",
            "text": '"He gave it back," Odin says quietly. "At the end. That matters."',
        },
    ],
    "choices": [
        {
            "label": '"Why does it matter?"',
            "next": "act3_the_memory",
            "effects": {"mercy": 3},
        },
        {
            "label": '"It does not change what you did."',
            "next": "act3_the_memory",
            "effects": {"honour": 3},
        },
        {
            "label": "Say nothing. Just hold the key.",
            "next": "act3_the_memory",
            "effects": {"resolve": 3},
        },
    ],
}

# ─────────────────────────────────────────────────────────────
#  ACT III END
# ─────────────────────────────────────────────────────────────

SCENE_ACT3_THE_MEMORY = {
    "art": "crossroads",
    "cinematic": True,
    "header": {
        "title": "THE NAMING",
        "subtitle": "what the dead keep",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "He steps back. Not away — he does not leave, exactly. "
                "He cedes the crossroads. "
                "As if the space belongs to you now, briefly, "
                "for as long as you need it."
            ),
        },
        {
            "type": "prose",
            "text": (
                "The fog has pulled back down one of the paths. "
                "Not much. Enough to see that something waits at the end of it. "
                "Not a shape — a quality. A density. "
                "The sense of things accumulated. Things waited-for. "
                "Things that have not yet been allowed to end."
            ),
        },
        {
            "type": "italic",
            "text": "The key is warm again. Not the warmth of memory. Something older.",
        },
        {
            "type": "memory",
            "key": "the_naming_rune",
            "label": "What the key is",
            "text": (
                "Your naming-rune. Carved by your father before you could speak. "
                "Given to Gunnar at a crossroads eleven years ago as surety for an oath. "
                "'If I break this — take it. Take my name with it.' "
                "Kept by him through campaigns and long service and everything you cost him. "
                "Returned at the moment of his ending. "
                "You hold it now and do not know yet what that means — "
                "whether it is a restoration or a question still open. "
                "You think it may be both."
            ),
        },
        {
            "type": "prose",
            "text": (
                "Odin is watching you the way the sea watches — "
                "not with intention, not without it. "
                "Simply present. Simply witness."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"Go," he says. '
                '"What is at the end of that path has been collecting '
                "the unfinished for longer than this war has been running. "
                "It will know what to do with you. "
                'Whether you want it to or not."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "The fog closes behind you as you walk — "
                "not like a door, but like the sea closing over a stone. "
                "Quietly. Completely."
            ),
        },
    ],
    "choices": [
        {
            "label": "Into the dark. Forward.",
            "next": "act_4_intro",
        },
    ],
}

SCENE_ACT_4_INTRO = {
    "art": "crossroads",
    "cinematic": True,
    "header": {
        "title": "ACT IV",
        "subtitle": "The Keeper of the Unfinished",
    },
    "beats": [
        {
            "type": "italic",
            "text": "Coming soon.",
        },
    ],
    "next": "act3_the_memory",
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
    "odin_appears": SCENE_ODIN_APPEARS,
    "odin_confrontation": SCENE_ODIN_CONFRONTATION,
    "odin_gunnar": SCENE_ODIN_GUNNAR,
    "odin_the_reason": SCENE_ODIN_THE_REASON,
    "odin_the_naming": SCENE_ODIN_THE_NAMING,
    "act3_the_memory": SCENE_ACT3_THE_MEMORY,
    "act_4_intro": SCENE_ACT_4_INTRO,
}
