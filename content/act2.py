# ============================================================
#  content/act2.py
#  Act II — The Stirring Beneath
#  Pure data. No logic. The engine in scene.py runs these.
# ============================================================

SCENE_FOG_ROAD = {
    "art": "fog_road",
    "header": {
        "title": "THE ROAD SOUTH",
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
            "next": "fog_the_held",
        },
        {
            "label": "Keep moving.",
            "next": "fog_the_held",
        },
        {
            "label": "Look at the key.",
            "next": "fog_the_held",
        },
        {
            "label": "Turn off the road. Into the trees.",
            "next": "forest_path",
            "effects": {"brutality": 2},
            "condition": {"not": {"flag": "forest_visited"}},
        },
    ],
}

SCENE_FOG_THE_HELD = {
    "art": "fog_road",
    "header": {
        "title": "THE HELD",
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
            "text": 'Her mouth opens. "Don\'t," she says. Not to you. To the man beside '
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
            "next": "fog_held_after",
        },
        {
            "label": 'Stay still. "I see you. You can let go."',
            "next": "fog_held_release",
        },
        {
            "label": "Look at the man. The other one hasn't moved.",
            "next": "fog_held_other",
        },
    ],
}

SCENE_FOG_HELD_OTHER = {
    "art": "fog_road",
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
            "next": "fog_held_after",
        },
        {
            "label": 'Speak to her. "You can let go. Both of you."',
            "next": "fog_held_release",
        },
    ],
}

SCENE_FOG_HELD_RELEASE = {
    "art": "fog_road",
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
            "text": '"How long," he says. Not a question. A statement he has said '
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
            "key": "held_released",
            "label": "What it costs to be seen",
            "text": "The woman's grip releasing. Finger by finger. The man finally "
            "turning his head. How long it took. How little it required.",
        },
        {
            "type": "stat",
            "changes": {"honour": 5},
        },
        {
            "type": "prose",
            "text": (
                "Before you go, you notice what the man was carrying at his side. "
                "A small shield — traveller's make, not a warrior's, "
                "but solid enough. He sets it down without looking at you. "
                "An offering. Or a release."
            ),
        },
        {"type": "item", "item": "traveller's shield", "action": "give"},
    ],
    "next": "fog_sentinel",
}

SCENE_FOG_HELD_AFTER = {
    "art": "fog_road",
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
            "key": "held_forced",
            "label": "The strength required to leave someone behind",
            "text": "The cold of her grip. How long it stayed. What it meant that "
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
            "key": "held_forced",
            "value": True,
        },
    ],
    "next": "fog_sentinel",
}

SCENE_FOG_SENTINEL = {
    "art": "fog_sentinel",
    "header": {
        "title": "THE FOG-SENTINEL",
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
            "next": "combat_fog_sentinel",
        },
        {
            "label": "Circle wide. Leave the road entirely.",
            "next": "fog_sentinel_avoided",
        },
        {
            "label": "Stand still. Wait.",
            "next": "fog_sentinel_wait",
        },
    ],
}

SCENE_FOG_SENTINEL_WAIT = {
    "art": "fog_sentinel",
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
            "next": "combat_fog_sentinel",
        },
        {
            "label": "Circle wide. Get off the road.",
            "next": "fog_sentinel_avoided",
        },
    ],
}

SCENE_FOG_SENTINEL_AVOIDED = {
    "art": "fog_sentinel",
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
            "key": "sentinel_avoided",
            "value": True,
        },
    ],
    "next": "fog_sentinel_after",
}

SCENE_COMBAT_FOG_SENTINEL = {
    "art": "fog_sentinel",
    "next": "gatehouse_approach",
    "header": {
        "title": "THE FOG-SENTINEL",
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
    "art": "fog_road",
    "beats": [
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": {"flag": "sentinel_avoided"},
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
    "art": "gatehouse",
    "header": {
        "title": "THE GATEHOUSE",
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
                    "condition": {"flag": "held_forced"},
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
                    "condition": {"flag": "held_forced"},
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
            "next": "gatehouse_guards_hostile",
            "condition": {"flag": "held_forced"},
        },
        {
            "label": "Step back. Give them space.",
            "next": "gatehouse_guards_hostile",
            "condition": {"flag": "held_forced"},
        },
        {
            "label": "Look at the guards closely.",
            "next": "gatehouse_guards",
            "condition": {"not": {"flag": "held_forced"}},
        },
        {
            "label": "Look at the courtyard ahead.",
            "next": "gatehouse_courtyard",
            "condition": {"not": {"flag": "held_forced"}},
        },
        {
            "label": "Touch the wall.",
            "next": "gatehouse_wall",
            "condition": {"not": {"flag": "held_forced"}},
        },
    ],
}

SCENE_GATEHOUSE_GUARDS_HOSTILE = {
    "art": "gatehouse",
    "header": {
        "title": "THE GATEHOUSE",
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
            "next": "gatehouse_guards_calmed",
            "effects": {"honour": 3},
        },
        {
            "label": '"I am not here to fight. I came through the fog alone."',
            "next": "gatehouse_guards_spoken",
        },
        {
            "label": "Show them Gunnar's Axe. Let them see whose it is.",
            "next": "gatehouse_guards_axe",
            "condition": {
                "and": [{"flag": "held_forced"}, {"equipped": "Gunnar's Axe"}]
            },
        },
        {
            "label": "Force your way through.",
            "next": "gatehouse_guards_forced",
            "effects": {"honour": -5, "brutality": 5},
        },
    ],
}

SCENE_GATEHOUSE_GUARDS_CALMED = {
    "art": "gatehouse",
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
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_GUARDS_SPOKEN = {
    "art": "gatehouse",
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
    "art": "gatehouse",
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
            "key": "guards_axe_recognition",
            "label": "What the axe still means to those who served under it",
            "text": "The guards stepping aside for the axe. "
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
    "art": "gatehouse",
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
            "key": "guards_forced",
            "value": True,
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_GUARDS = {
    "art": "gatehouse",
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
            "key": "guards_recognised",
            "label": "Where you have seen that stillness before",
            "text": "The guards at the gate. The angle of their shoulders. "
            "The particular stillness of men trained by the same hand.",
        },
        {
            "type": "flag",
            "key": "guards_examined",
            "value": True,
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_COURTYARD = {
    "art": "gatehouse",
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
    "art": "gatehouse",
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
            "key": "wall_warmth",
            "label": "Something about warmth in the wrong place",
            "text": "The stone of the gatehouse wall. How warm it was. "
            "What kind of warmth that was.",
        },
    ],
    "next": "gatehouse_inside",
}

SCENE_GATEHOUSE_INSIDE = {
    "art": "gatehouse",
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
            "text": '"I wondered which door you would use."',
        },
    ],
    "next": "great_hall_entrance",
}

# ═════════════════════════════════════════════════════════════
#  ACT II — THE GREAT HALL / ODRIK
# ═════════════════════════════════════════════════════════════

SCENE_GREAT_HALL_ENTRANCE = {
    "art": "great_hall",
    "header": {
        "title": "THE GREAT HALL",
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
                    "condition": {"not": {"flag": "odrik_met"}},
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
                    "condition": {"not": {"flag": "odrik_met"}},
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
                    "condition": {"not": {"flag": "odrik_met"}},
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
                    "condition": {"not": {"flag": "odrik_met"}},
                    "text": (
                        "He does not look up when you approach. " "He speaks first."
                    ),
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": {"not": {"flag": "odrik_met"}},
                    "text": (
                        '"You came alone," he says. '
                        '"I did not know if you would come alone."'
                    ),
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": {"not": {"flag": "odrik_met"}},
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
                    "condition": {
                        "and": [
                            {"not": {"flag": "odrik_met"}},
                            {"flag": "defeated_fog_sentinel"},
                        ]
                    },
                    "text": '"You fought the Sentinel."',
                },
                {
                    "condition": {
                        "and": [
                            {"not": {"flag": "odrik_met"}},
                            {"flag": "sentinel_avoided"},
                        ]
                    },
                    "text": '"You walked past the Sentinel."',
                },
                {
                    "condition": {"not": {"flag": "odrik_met"}},
                    "text": '"You ran from the Sentinel."',
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": {"not": {"flag": "odrik_met"}},
                    "text": "Still he does not look up.",
                },
            ],
        },
        {
            "type": "conditional_prose",
            "variants": [
                {
                    "condition": {"not": {"flag": "odrik_met"}},
                    "text": (
                        '"I heard the bell stop. '
                        "I have been listening for that sound "
                        'for a very long time."'
                    ),
                },
            ],
        },
    ],
    "choices": [
        {
            "label": "Say nothing. Wait.",
            "next": "odrik_silence",
            "condition": {"not": {"flag": "odrik_met"}},
        },
        {
            "label": '"Then you knew I was coming."',
            "next": "odrik_knew",
            "condition": {"not": {"flag": "odrik_met"}},
        },
        {
            "label": '"What are you?"',
            "next": "odrik_what_are_you",
            "condition": {"not": {"flag": "odrik_met"}},
        },
        {
            "label": "Examine the door frame.",
            "next": "great_hall_rune_door",
            "condition": {
                "and": [
                    {"flag": "odrik_met"},
                    {"flag": "odrik_place_seen"},
                    {"memory": "odrik_purpose"},
                    {"memory": "the_key_origin"},
                    {"not": {"flag": "rune_door_seen"}},
                ]
            },
        },
        {
            "label": "Return to Odrik.",
            "next": "odrik_first_questions",
            "condition": {"flag": "odrik_met"},
        },
        {
            "label": "Leave the hall. Continue forward.",
            "next": "act2_end",
            "condition": {"flag": "odrik_sent_forward"},
        },
    ],
}

SCENE_ODRIK_SILENCE = {
    "art": "great_hall",
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
                '"Good," he says. '
                "Not approval, exactly. "
                "More like confirmation of something he suspected."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"Gunnar said you listened before you spoke. '
                "Most people don't. "
                'It is why he trusted you."'
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
    "art": "great_hall",
    "beats": [
        {
            "type": "prose",
            "text": "He looks up for the first time.",
        },
        {
            "type": "italic",
            "text": (
                '"I knew someone would come," he says. '
                '"I did not know it would be you '
                'until the Sentinel stopped."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"That thing tests what belongs here '
                "and what does not. "
                "The dead belong here — they cannot leave. "
                "The living do not belong — they cannot enter. "
                'You are neither."'
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
            "text": ('"That narrows it considerably," ' 'he says. "To one person."'),
        },
    ],
    "next": "odrik_measures_you",
}

SCENE_ODRIK_WHAT_ARE_YOU = {
    "art": "great_hall",
    "beats": [
        {
            "type": "prose",
            "text": "That makes him look up.",
        },
        {
            "type": "italic",
            "text": (
                '"An interesting first question," he says. '
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
                'because he asked me to."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"What I am now — '
                "that is a more difficult question. "
                "I have had considerable time to consider it "
                'and I do not yet have a satisfying answer."'
            ),
        },
        {
            "type": "prose",
            "text": ("He looks at you steadily. " "He is deciding something."),
        },
    ],
    "next": "odrik_measures_you",
}

SCENE_ODRIK_MEASURES_YOU = {
    "art": "great_hall",
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
                    "condition": {"equipped": "Gunnar's Axe"},
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
                    "condition": {"equipped": "Gunnar's Axe"},
                    "text": (
                        '"He gave it to you," Odrik says. '
                        "Flat. Careful. "
                        '"Or you took it."'
                    ),
                },
                {
                    "condition": None,
                    "text": (
                        '"You have been on the battlefield," '
                        'he says. "You found things."'
                    ),
                },
            ],
        },
        {
            "type": "italic",
            "text": (
                '"Sit down," he says. '
                '"I will answer what I can. '
                'I cannot promise it will be everything."'
            ),
        },
        {
            "type": "flag",
            "key": "odrik_met",
            "value": True,
        },
    ],
    "next": "odrik_first_questions",
}

SCENE_ODRIK_FIRST_QUESTIONS = {
    "art": "great_hall",
    "header": {
        "title": "ODRIK THE BOUND",
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
            "label": '"What is this place?"',
            "next": "odrik_explains_place",
        },
        {
            "label": 'Show him the key. "The rune is incomplete."',
            "next": "odrik_the_night",
            "condition": {
                "and": [
                    {"flag": "rune_door_seen"},
                    {"not": {"flag": "odrik_night_confronted"}},
                ]
            },
        },
        {
            "label": '"What does the key open?"',
            "next": "odrik_the_key",
            "condition": {"has_item": "Remembrance Key"},
        },
        {
            "label": '"Why are you still here?"',
            "next": "odrik_why_bound",
        },
        {
            "label": '"Why can\'t you tell me?"',
            "next": "odrik_go_forward",
            "condition": {
                "and": [
                    {"flag": "odrik_night_confronted"},
                    {"not": {"flag": "odrik_sent_forward"}},
                ]
            },
        },
        {
            "label": "Leave Odrik for now. Look around the hall.",
            "next": "great_hall_entrance",
        },
    ],
}

SCENE_ODRIK_EXPLAINS_PLACE = {
    "art": "great_hall",
    "beats": [
        {
            "type": "italic",
            "text": (
                '"It is a place between," he says. '
                '"Between dying and being dead. '
                'Between what happened and what it meant."'
            ),
        },
        {
            "type": "prose",
            "text": ("He looks at the frozen men around them."),
        },
        {
            "type": "italic",
            "text": (
                '"They are held here. '
                "Not imprisoned — held. "
                "There is a difference. "
                "A prison keeps you against your will. "
                "This holds you because something is unfinished. "
                "Something they were part of "
                'that has not resolved."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"The battlefield. The longhouse. '
                "This hall. "
                "All of it is the same thing — "
                "a moment that refuses to end "
                'because it was not allowed to end properly."'
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
            "text": '"You are here to end it."',
        },
        {
            "type": "prose",
            "text": ("Not a question. " "But not entirely certain either."),
        },
        {
            "type": "flag",
            "key": "odrik_place_seen",
            "value": True,
        },
    ],
    "next": "odrik_first_questions",
}

SCENE_ODRIK_THE_NIGHT = {
    "art": "great_hall",
    "beats": [
        {
            "type": "prose",
            "text": ("You hold out the key. " "Not as a threat — you let him see it."),
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
            "type": "memory",
            "key": "the_key_recognized",
            "label": "What the key did to Odrik",
            "text": (
                "When he saw the key, something in him moved that he did not choose to move. "
                "Not recognition. Not fear. "
                "The structure beneath him — the same structure as the rune — "
                "responded. As if the key and the binding share a root "
                "he has spent forty years trying not to think about."
            ),
        },
        {
            "type": "italic",
            "text": '"The rune is incomplete."',
        },
        {
            "type": "prose",
            "text": (
                "He looks at you for the first time " "without first calculating."
            ),
        },
        {
            "type": "italic",
            "text": '"Then why does it hold?"',
        },
        {
            "type": "prose",
            "text": "You know the answer. You saw it in the door frame.",
        },
        {
            "type": "italic",
            "text": '"Because something else is finishing it."',
        },
        {
            "type": "prose",
            "text": "Silence.",
        },
        {
            "type": "prose",
            "text": (
                "Odrik sets the cup down. " "He has not set it down once until now."
            ),
        },
        {
            "type": "memory",
            "key": "rune_not_alone",
            "label": "What the rune is connected to",
            "text": (
                "The rune at the door is incomplete. And yet it holds. "
                "Because something else is finishing it. "
                "You said it before you fully understood it. "
                "Odrik set down the cup."
            ),
        },
        {
            "type": "flag",
            "key": "odrik_night_confronted",
            "value": True,
        },
    ],
    "next": "odrik_first_questions",
}

SCENE_ODRIK_THE_KEY = {
    "art": "great_hall",
    "beats": [
        {
            "type": "prose",
            "text": "He goes very still.",
        },
        {
            "type": "italic",
            "text": ('"Show me."'),
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
                '"I made that," he says quietly. '
                '"Eleven years ago. '
                "Before any of this. "
                'Before I knew what it would be needed for."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"It is not a key to a place. '
                "It is a key to a memory — "
                "specifically, to yours. "
                "It was made from something of yours "
                "that Gunnar kept. "
                "Something you gave him "
                'the night you swore the oath."'
            ),
        },
        {
            "type": "prose",
            "text": ("He sits back. " "He is watching your face."),
        },
        {
            "type": "italic",
            "text": (
                '"You don\'t remember giving it to him," '
                'he says. "Not yet. '
                'You will."'
            ),
        },
        {
            "type": "memory",
            "key": "the_key_origin",
            "label": "What the key is made from",
            "text": (
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
    "art": "great_hall",
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
            "text": ("As if the pattern continues beyond what the eye can follow."),
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
            "key": "rune_door",
            "label": "What is holding the hall together",
            "text": (
                "The runes at the door frame. Cut too deep, incomplete, and yet — "
                "they hold. Not a seal. Not a lock. "
                "A structure that keeps the moment from ending. "
                "Someone made this. Someone who knew exactly what they were doing."
            ),
        },
        {
            "type": "flag",
            "key": "rune_door_seen",
            "value": True,
        },
    ],
    "next": "great_hall_entrance",
}

SCENE_ODRIK_WHY_BOUND = {
    "art": "great_hall",
    "beats": [
        {
            "type": "italic",
            "text": ('"Because I have not done ' 'what I came here to do," he says.'),
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
                'and I could not stop it."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"The binding is not a punishment. '
                "It is an unfinished sentence. "
                'I cannot leave until the sentence is finished."'
            ),
        },
        {
            "type": "prose",
            "text": ("He looks at you steadily."),
        },
        {
            "type": "italic",
            "text": (
                '"You finishing it '
                "and me finishing it "
                "are the same thing. "
                'That is why I have been waiting for you."'
            ),
        },
        {
            "type": "memory",
            "key": "odrik_purpose",
            "label": "Why Odrik is bound",
            "text": (
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

SCENE_ACT2_END = {
    "art": "great_hall",
    "header": {
        "title": "ACT II COMPLETE",
        "subtitle": "The Stirring Beneath",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "You leave the hall the way you entered it. "
                "The frozen men do not turn. "
                "The food does not spoil. "
                "The candles do not move."
            ),
        },
        {
            "type": "prose",
            "text": (
                "Behind you, Odrik sits at the head table "
                "with the cup still resting where he left it. "
                "He does not call after you. "
                "He knew you would go."
            ),
        },
        {
            "type": "italic",
            "text": ("The rune is not alone. " "Follow what it is connected to."),
        },
        {
            "type": "prose",
            "text": (
                "Beyond the gatehouse, the fog is different. "
                "Not thinner — deeper. "
                "As if the further south you go, "
                "the more the fog has to say."
            ),
        },
        {
            "type": "italic",
            "text": "The key is warm in your hand. It has been warm since the hall.",
        },
    ],
    "choices": [
        {
            "label": "Continue. Follow the rune.",
            "next": "act_3_intro",
            "effects": {"resolve": 10},
        },
    ],
}

SCENE_ACT_3_INTRO = {
    "art": "act_break",
    "header": {
        "title": "ACT III",
        "subtitle": "The Silence Beneath",
    },
    "beats": [
        {
            "type": "italic",
            "text": "Coming soon.",
        },
    ],
    "choices": [
        {
            "label": "Return to the hall (restart Act 2).",
            "next": "__restart__",
        },
    ],
}

SCENE_ODRIK_GO_FORWARD = {
    "art": "odrik_go_forward",
    "beats": [
        {
            "type": "prose",
            "text": (
                "He looks at where the cup was. " "As if its absence means something."
            ),
        },
        {
            "type": "italic",
            "text": ('"I was there. I saw all of it."'),
        },
        {
            "type": "prose",
            "text": "A pause.",
        },
        {
            "type": "italic",
            "text": (
                '"There are things I cannot say. '
                "Not because I choose silence — "
                "the binding holds those words. "
                'They exist in me but they cannot come out."'
            ),
        },
        {
            "type": "italic",
            "text": (
                '"But they exist somewhere else too. '
                "In this building. "
                'In what was left behind."'
            ),
        },
        {
            "type": "prose",
            "text": ("He meets your eyes."),
        },
        {
            "type": "italic",
            "text": ('"The rune is not alone. ' 'Follow what it is connected to."'),
        },
        {
            "type": "italic",
            "text": (
                '"You will find out what happened. '
                "Not from me. "
                'From the place itself."'
            ),
        },
        {
            "type": "flag",
            "key": "odrik_sent_forward",
            "value": True,
        },
    ],
    "next": "great_hall_entrance",
}


# ─────────────────────────────────────────────────────────────
#  HERMIT'S TRIAL — forest path off the fog road
# ─────────────────────────────────────────────────────────────

SCENE_FOREST_PATH = {
    "art": "forest",
    "header": {
        "title": "THE DARK WOOD",
        "subtitle": "the trees remember the war",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "A gap between the fog and the treeline — barely a path, "
                "more a suggestion. The trees here are old. "
                "Not tall, but dense, the kind of density that comes from "
                "centuries of competing for the same light. "
                "Their roots have pulled up the ground around them. "
                "The mud between them is darker than the mud on the road."
            ),
        },
        {
            "type": "italic",
            "text": (
                "Something moves between the trees. " "Low. Pale. Not in a hurry."
            ),
        },
        {"type": "flag", "key": "forest_visited"},
        {
            "type": "memory",
            "key": "the_dark_wood",
            "label": "The path into the dark wood",
            "text": (
                "The trees were old and dense and did not want you there. "
                "You went in anyway. "
                "Something pale moved between them, ahead of you, "
                "neither fleeing nor following."
            ),
        },
    ],
    "choices": [
        {
            "label": "Press deeper into the wood.",
            "next": "forest_wolf",
            "effects": {"resolve": -3},
        },
        {
            "label": "Turn back to the road.",
            "next": "fog_road",
        },
    ],
}

SCENE_FOREST_WOLF = {
    "art": "combat_dire_wolf",
    "beats": [
        {
            "type": "prose",
            "text": (
                "It steps out from behind a root mass the size of a cart. "
                "Larger than it should be — the fog has done something to it, "
                "or the years have, or both. "
                "Its coat is the colour of old ash. "
                "It does not growl. It simply looks at you, and waits."
            ),
        },
        {
            "type": "memory",
            "key": "wolf_of_odin_sight",
            "label": "Odin's Wolf",
            "text": (
                "The ulfhednar wore wolf pelts and became the thing beneath the skin. "
                "You have heard that some wolves go the other way — "
                "that Odin's hunger walks inside them instead of a man. "
                "The wolf in front of you does not behave like an animal. "
                "It behaves like something waiting to be recognised. "
                "The old stories say Odin's creatures do not just wound — "
                "they take. The runes in your bones feel colder already."
            ),
        },
        {
            "type": "combat",
            "enemy": "wolf",
            "variant": "dire",
        },
        {"type": "stat", "changes": {"resolve": 5}},
        {
            "type": "memory",
            "key": "wolf_of_odin_killed",
            "label": "What the Wolf Left Behind",
            "text": (
                "It did not die like an animal. "
                "There was a moment — between the last breath and the stillness — "
                "when something passed out of it that had not been wolf. "
                "You do not know if killing it was right. "
                "You know only that it is done."
            ),
        },
    ],
    "choices": [
        {
            "label": "Take the wolf pelt.",
            "next": "forest_wolf_pelt",
            "condition": {"not": {"has_item": "wolf pelt"}},
        },
        {
            "label": "Press deeper into the dark wood.",
            "next": "forest_bear",
        },
        {
            "label": "Make for the great oak.",
            "next": "hermit_oak",
        },
    ],
}

SCENE_FOREST_WOLF_PELT = {
    "art": "combat_dire_wolf",
    "beats": [
        {
            "type": "prose",
            "text": (
                "The pelt is heavy and cold. "
                "You pull it across your shoulders. "
                "It settles like a second skin — "
                "like something that was waiting for someone to put it on again."
            ),
        },
        {"type": "item", "action": "give", "name": "wolf pelt"},
    ],
    "choices": [
        {
            "label": "Press deeper into the dark wood.",
            "next": "forest_bear",
        },
        {
            "label": "Make for the great oak.",
            "next": "hermit_oak",
        },
    ],
}

SCENE_FOREST_BEAR = {
    "art": "combat_bear",
    "beats": [
        {
            "type": "prose",
            "text": (
                "The trees open into a hollow — a natural ring where nothing grows. "
                "At the centre, a shape. "
                "It is sitting. Not crouching, not sleeping: sitting, "
                "the way a man sits when he has stopped caring about comfort. "
                "When it turns toward you, its eyes are wrong. "
                "Not animal-wrong. Something older."
            ),
        },
        {
            "type": "italic",
            "text": (
                "You remember something your father said: "
                "the berserkir did not go mad. They were emptied. "
                "The god filled what was left."
            ),
        },
        {
            "type": "memory",
            "key": "bear_of_odin_sight",
            "label": "The Berserker's Skin",
            "text": (
                "The berserkir wore bear pelts into battle and became something else — "
                "not animal, not man, but whatever stood between them. "
                "Odin's rage made flesh. "
                "The bear in the hollow sits like a warrior between charges. "
                "You do not know if the man is still inside it, "
                "or if the hide was all that was left."
            ),
        },
    ],
    "choices": [
        {
            "label": "Step into the hollow.",
            "next": "forest_bear_fight",
            "effects": {"brutality": 2},
        },
        {
            "label": "Back away slowly.",
            "next": "forest_bear_avoided",
            "effects": {"resolve": 2},
        },
    ],
}

SCENE_FOREST_BEAR_FIGHT = {
    "art": "combat_bear",
    "beats": [
        {
            "type": "combat",
            "enemy": "bear",
            "variant": "berserker",
        },
        {"type": "stat", "changes": {"resolve": 7, "brutality": 3}},
        {
            "type": "memory",
            "key": "bear_of_odin_killed",
            "label": "What the Bear Carried",
            "text": (
                "When it fell, the rage left the air around it. "
                "Whatever had been riding it — god or memory or something with no name — "
                "was gone. "
                "The hollow felt ordinary after that. "
                "Just trees and mud and a dead animal. "
                "That felt worse, somehow."
            ),
        },
    ],
    "choices": [
        {
            "label": "Take the bear pelt.",
            "next": "forest_bear_pelt",
            "condition": {"not": {"has_item": "bear pelt"}},
        },
        {
            "label": "Make for the great oak.",
            "next": "hermit_oak",
        },
    ],
}

SCENE_FOREST_BEAR_PELT = {
    "art": "combat_bear",
    "beats": [
        {
            "type": "prose",
            "text": (
                "The pelt is enormous. You have never touched anything like it — "
                "the weight of it, the warmth still in it. "
                "When you pull it over your shoulders "
                "something shifts behind your eyes. "
                "Not wrong. Not right. Different."
            ),
        },
        {"type": "item", "action": "give", "name": "bear pelt"},
    ],
    "next": "hermit_oak",
}

SCENE_FOREST_BEAR_AVOIDED = {
    "art": "combat_bear",
    "beats": [
        {
            "type": "prose",
            "text": (
                "You take one step back. Then another. "
                "The bear does not move. It watches you — "
                "not with hunger, not with fear. "
                "With something that has no animal name. "
                "You reach the treeline and it is still sitting, "
                "still watching, as the hollow closes behind you."
            ),
        },
        {
            "type": "memory",
            "key": "bear_of_odin_left",
            "label": "The Bear You Left",
            "text": (
                "It did not follow. "
                "You do not know if that was mercy or indifference — "
                "whether you chose to leave, or whether it let you go. "
                "The distinction feels important and you cannot resolve it."
            ),
        },
    ],
    "next": "hermit_oak",
}

SCENE_HERMIT_OAK = {
    "art": "hermit_oak",
    "header": {
        "title": "THE GREAT OAK",
        "subtitle": "older than the war",
    },
    "beats": [
        {
            "type": "prose",
            "text": (
                "The tree at the centre of the wood is enormous — "
                "not tall but wide, its trunk wider than three men standing arms out. "
                "Runes have been carved into the bark, but not recently. "
                "The wood has grown around them, half-swallowing the marks. "
                "Whoever made them is long past caring whether they are read."
            ),
        },
        {
            "type": "memory",
            "key": "the_great_oak",
            "label": "The oak at the centre of things",
            "text": (
                "A tree that was old when the war began. "
                "Runes in the bark, half-swallowed. "
                "The roots run deeper than the dead."
            ),
        },
        {
            "type": "prose",
            "text": (
                "At the base of the oak, cross-legged and apparently asleep, "
                "sits a man. Old — genuinely old, the kind of old that seems "
                "deliberate. A staff across his knees. "
                "He does not look dead. He does not look like he belongs here either. "
                "He looks like he chose this."
            ),
        },
        {
            "type": "italic",
            "text": "He opens one eye.",
        },
    ],
    "choices": [
        {
            "label": "Speak to him.",
            "next": "hermit_greet",
        },
        {
            "label": "Leave the wood. Back to the road.",
            "next": "fog_sentinel",
            "effects": {"resolve": 2},
        },
    ],
}

SCENE_HERMIT_GREET = {
    "art": "hermit_oak",
    "beats": [
        {
            "type": "italic",
            "text": '"You killed the wolf," he says. Not a question.',
        },
        {
            "type": "prose",
            "text": (
                "He opens the other eye. Studies you with the particular attention "
                "of someone who has been waiting for something, and is not yet sure "
                "if this is it."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"It has been here longer than I have. I fed it, when I could. '
                'It was not grateful. Animals rarely are." '
                "He pauses. "
                '"You are not from the road."'
            ),
        },
    ],
    "choices": [
        {
            "label": '"I woke on the battlefield."',
            "next": "hermit_battlefield",
            "effects": {"honour": 3},
        },
        {
            "label": '"Who are you?"',
            "next": "hermit_who",
        },
        {
            "label": "Say nothing. Watch him.",
            "next": "hermit_silence",
            "effects": {"resolve": 2},
        },
        {
            "label": '"This pelt. I cannot take it off."',
            "next": "hermit_bear_pelt",
            "condition": {"has_item": "bear pelt"},
        },
    ],
}

SCENE_HERMIT_BEAR_PELT = {
    "art": "hermit_oak",
    "beats": [
        {
            "type": "prose",
            "text": (
                "He does not look at the pelt. He looks at you — at your hands, "
                "at the set of your jaw, at the way you are standing. "
                "Then he looks at the pelt."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"The berserkir did not wear the hide," he says. '
                '"The hide wore them. There is a difference." '
                "He stands. For an old man leaning against a tree, "
                "he moves without difficulty. "
                '"Hold still."'
            ),
        },
        {
            "type": "prose",
            "text": (
                "He speaks no words you recognise. "
                "His hands do not touch the pelt but move around it — "
                "tracing something in the air that you cannot see. "
                "The weight across your shoulders shifts, "
                "like a breath held for too long finally released. "
                "The pelt falls. "
                "It hits the ground and lies there, ordinary."
            ),
        },
        {"type": "item", "action": "take", "name": "bear pelt"},
        {"type": "stat", "changes": {"resolve": 5, "brutality": -5}},
        {
            "type": "memory",
            "key": "hermit_bear_pelt",
            "label": "What the Hermit said about the hide",
            "text": (
                "The hide wore them. Not the other way. "
                "He said it like the distinction mattered — "
                "like it was the difference between a wound and a scar."
            ),
        },
        {
            "type": "italic",
            "text": (
                "He returns to his place against the oak. "
                '"The god\u2019s hunger goes looking for another vessel now. '
                'Do not be in the wood at night." '
                "He closes his eyes."
            ),
        },
    ],
    "choices": [
        {
            "label": '"Thank you."',
            "next": "hermit_greet",
            "effects": {"honour": 3},
        },
        {
            "label": "Say nothing. Return to the road.",
            "next": "hermit_depart",
        },
    ],
}

SCENE_HERMIT_BATTLEFIELD = {
    "art": "hermit_oak",
    "beats": [
        {
            "type": "italic",
            "text": (
                "He nods slowly, as if this confirms something. "
                '"The battlefield sends them sometimes. Not often. '
                'Usually the ones who had something unfinished." '
                "He looks at your hands. "
                '"What did you leave undone?"'
            ),
        },
    ],
    "choices": [
        {
            "label": '"I don\'t remember."',
            "next": "hermit_depart",
            "effects": {"resolve": -2},
        },
        {
            "label": '"An oath. I broke an oath."',
            "next": "hermit_oath",
            "effects": {"honour": 5},
            "condition": {"flag": "leif_done"},
        },
        {
            "label": "Leave him. Back to the road.",
            "next": "fog_sentinel",
        },
    ],
}

SCENE_HERMIT_WHO = {
    "art": "hermit_oak",
    "beats": [
        {
            "type": "italic",
            "text": (
                '"No one, now. I was a skald once. '
                "Then a soldier. Then a penitent. "
                'Now I sit under a tree and feed wolves." '
                "He almost smiles. "
                '"The last stage suits me best."'
            ),
        },
    ],
    "choices": [
        {
            "label": '"Why here?"',
            "next": "hermit_why",
        },
        {
            "label": "Leave him. Back to the road.",
            "next": "fog_sentinel",
        },
    ],
}

SCENE_HERMIT_WHY = {
    "art": "hermit_oak",
    "beats": [
        {
            "type": "italic",
            "text": (
                "He looks up at the oak. "
                '"Because the tree asked. Not in words. '
                "Trees do not use words. "
                'But it asked." '
                "He is quiet for a moment. "
                '"The battlefield keeps its dead. '
                "The wood keeps its living. "
                'I am somewhere between."'
            ),
        },
    ],
    "next": "hermit_depart",
}

SCENE_HERMIT_SILENCE = {
    "art": "hermit_oak",
    "beats": [
        {
            "type": "italic",
            "text": (
                "He seems to approve of this. "
                '"Most of them talk immediately. '
                'The ones who wait usually know something worth waiting for." '
                "He rises, slowly, joints announcing themselves. "
                '"Walk with me."'
            ),
        },
        {"type": "stat", "changes": {"resolve": 3}},
    ],
    "next": "hermit_depart",
}

SCENE_HERMIT_OATH = {
    "art": "hermit_oak",
    "beats": [
        {
            "type": "italic",
            "text": (
                "Something shifts in his expression. Not pity. "
                "Recognition. "
                '"An oath to whom?"',
            ),
        },
        {
            "type": "prose",
            "text": (
                "You tell him what you remember. "
                "He listens the way old people listen — "
                "completely, without interrupting, without reassuring. "
                "When you finish he is quiet for a long time."
            ),
        },
        {
            "type": "italic",
            "text": (
                '"The battlefield keeps you because the oath is not finished. '
                "Not broken — unfinished. "
                'There is a difference." '
                "He hands you something small and cold. "
                '"Keep this. You will know when to use it."'
            ),
        },
        {"type": "item", "item": "runic token", "action": "give"},
        {"type": "stat", "changes": {"honour": 5, "resolve": 5}},
        {
            "type": "memory",
            "key": "hermit_oath",
            "label": "The Hermit's words on oaths",
            "text": (
                "Not broken — unfinished. There is a difference. "
                "He said it like it mattered."
            ),
        },
    ],
    "next": "hermit_depart",
}

SCENE_HERMIT_DEPART = {
    "art": "hermit_oak",
    "beats": [
        {
            "type": "prose",
            "text": (
                "He settles back against the oak, closes his eyes again. "
                "The conversation is over — not because he ended it, "
                "but because he has returned to whatever he was doing before you arrived. "
                "The tree seems larger now that you are leaving it."
            ),
        },
    ],
    "choices": [
        {
            "label": "Back to the road.",
            "next": "fog_sentinel",
            "effects": {"resolve": 2},
        },
    ],
}


SCENES = {
    "fog_road": SCENE_FOG_ROAD,
    "forest_path": SCENE_FOREST_PATH,
    "forest_wolf": SCENE_FOREST_WOLF,
    "forest_bear": SCENE_FOREST_BEAR,
    "forest_bear_fight": SCENE_FOREST_BEAR_FIGHT,
    "forest_bear_pelt": SCENE_FOREST_BEAR_PELT,
    "forest_bear_avoided": SCENE_FOREST_BEAR_AVOIDED,
    "forest_wolf_pelt": SCENE_FOREST_WOLF_PELT,
    "hermit_oak": SCENE_HERMIT_OAK,
    "hermit_greet": SCENE_HERMIT_GREET,
    "hermit_bear_pelt": SCENE_HERMIT_BEAR_PELT,
    "hermit_battlefield": SCENE_HERMIT_BATTLEFIELD,
    "hermit_who": SCENE_HERMIT_WHO,
    "hermit_why": SCENE_HERMIT_WHY,
    "hermit_silence": SCENE_HERMIT_SILENCE,
    "hermit_oath": SCENE_HERMIT_OATH,
    "hermit_depart": SCENE_HERMIT_DEPART,
    "fog_the_held": SCENE_FOG_THE_HELD,
    "fog_held_other": SCENE_FOG_HELD_OTHER,
    "fog_held_release": SCENE_FOG_HELD_RELEASE,
    "fog_held_after": SCENE_FOG_HELD_AFTER,
    "fog_sentinel": SCENE_FOG_SENTINEL,
    "fog_sentinel_wait": SCENE_FOG_SENTINEL_WAIT,
    "fog_sentinel_avoided": SCENE_FOG_SENTINEL_AVOIDED,
    "combat_fog_sentinel": SCENE_COMBAT_FOG_SENTINEL,
    "fog_sentinel_after": SCENE_FOG_SENTINEL_AFTER,
    "gatehouse_approach": SCENE_GATEHOUSE_APPROACH,
    "gatehouse_guards": SCENE_GATEHOUSE_GUARDS,
    "gatehouse_guards_hostile": SCENE_GATEHOUSE_GUARDS_HOSTILE,
    "gatehouse_guards_calmed": SCENE_GATEHOUSE_GUARDS_CALMED,
    "gatehouse_guards_spoken": SCENE_GATEHOUSE_GUARDS_SPOKEN,
    "gatehouse_guards_axe": SCENE_GATEHOUSE_GUARDS_AXE,
    "gatehouse_guards_forced": SCENE_GATEHOUSE_GUARDS_FORCED,
    "gatehouse_courtyard": SCENE_GATEHOUSE_COURTYARD,
    "gatehouse_wall": SCENE_GATEHOUSE_WALL,
    "gatehouse_inside": SCENE_GATEHOUSE_INSIDE,
    "great_hall_entrance": SCENE_GREAT_HALL_ENTRANCE,
    "great_hall_rune_door": SCENE_GREAT_HALL_RUNE_DOOR,
    "odrik_silence": SCENE_ODRIK_SILENCE,
    "odrik_knew": SCENE_ODRIK_KNEW,
    "odrik_what_are_you": SCENE_ODRIK_WHAT_ARE_YOU,
    "odrik_measures_you": SCENE_ODRIK_MEASURES_YOU,
    "odrik_first_questions": SCENE_ODRIK_FIRST_QUESTIONS,
    "odrik_explains_place": SCENE_ODRIK_EXPLAINS_PLACE,
    "odrik_the_night": SCENE_ODRIK_THE_NIGHT,
    "odrik_the_key": SCENE_ODRIK_THE_KEY,
    "odrik_why_bound": SCENE_ODRIK_WHY_BOUND,
    "odrik_go_forward": SCENE_ODRIK_GO_FORWARD,
    "act2_end": SCENE_ACT2_END,
    "act_3_intro": SCENE_ACT_3_INTRO,
}
