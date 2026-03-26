# ============================================================
#  content/enemies.py
#  Enemy definitions consumed by the combat engine.
#  Add new enemies here — no engine changes needed.
#
#  Fields:
#    name / name_short  — display strings
#    hp                 — starting hit points
#    damage             — (min, max) per hit
#    accuracy           — hit probability (0.0–1.0)
#    shards             — (min, max) echo shards dropped on death
#    loot               — [(item_name, probability), ...]
#    on_death           — optional side effects on enemy death:
#                           "flag":   flag key to set True
#                           "memory": (key, label) to add
#    phrases            — combat text pools (windup/hit/miss/death,
#                         plus special keys used by engine features)
#
#  Optional combat feature flags:
#    shield       — enemy has a shield; damage +5/+8 until flanked
#    drain        — hits drain player wrath and partially heal enemy
#    drain_amount — wrath drained per hit (default 0)
#    phases       — boss phase count (int); enables phase transitions
#    weapon       — dict {"name": "...", "effect": "bleeding"}; causes
#                   effect on player when enemy hits
#    variants     — dict of named stat overrides; activated via
#                   {"type": "combat", "enemy": "key", "variant": "name"}
#                   Any field can be overridden (hp, damage, weapon, etc.)
# ============================================================

ENEMIES = {
    "wolf": {
        "name":       "a Pale Wolf",
        "name_short": "the Wolf",
        "hp":         35,
        "damage":     (10, 18),
        "accuracy":   0.75,
        "weapon":     {"name": "bite", "effect": "bleeding"},
        "shards":     (40, 80),
        "loot":       [("wolf pelt", 0.6)],
        "variants": {
            "pack_leader": {
                "name":     "the Pack Leader",
                "hp":       55,
                "damage":   (14, 24),
                "accuracy": 0.80,
                "weapon":   {"name": "bite", "effect": "bleeding"},
            },
            "starved": {
                "name":     "a Starved Wolf",
                "hp":       22,
                "damage":   (12, 20),
                "accuracy": 0.82,
            },
            "dire": {
                "name":     "a Dire Wolf",
                "hp":       70,
                "damage":   (18, 30),
                "accuracy": 0.78,
                "weapon":   {"name": "maw", "effect": "bleeding"},
            },
            "silver": {
                "name":     "a Silver Wolf",
                "hp":       45,
                "damage":   (12, 22),
                "accuracy": 0.88,
            },
        },
        "phrases": {
            "windup": [
                "The wolf circles low, its eyes flat and pale. It is not afraid of you.",
                "It feints left — fast, faster than you expected.",
                "It drops its head and charges without warning.",
            ],
            "hit": [
                "The jaws find your arm. The grip is a vice.",
                "It hits low and you go down on one knee.",
                "Teeth in your side. You feel the warmth before the pain.",
            ],
            "miss": [
                "You throw your arm up. It snaps on air.",
                "You sidestep. It overshoots and scrambles to turn.",
                "It lunges — you move — its teeth click shut on nothing.",
            ],
            "death": [
                "It folds without a sound. The pale eyes go dark.",
                "The wolf lies still. It chose the wrong battlefield.",
                "It was hungry. That was all. Now it is not.",
            ],
        },
    },

    "rat": {
        "name":       "a Battlefield Rat",
        "name_short": "the Rat",
        "hp":         15,
        "damage":     (4, 9),
        "accuracy":   0.80,
        "shards":     (10, 30),
        "loot":       [],
        "variants": {
            "giant": {
                "name":     "a Giant Rat",
                "hp":       30,
                "damage":   (8, 15),
                "accuracy": 0.75,
                "weapon":   {"name": "bite", "effect": "bleeding"},
            },
            "plague": {
                "name":     "a Plague Rat",
                "hp":       18,
                "damage":   (6, 12),
                "accuracy": 0.78,
                "weapon":   {"name": "bite", "effect": "bleeding"},
            },
            "swarm": {
                "name":     "a Rat Swarm",
                "hp":       50,
                "damage":   (10, 16),
                "accuracy": 0.85,
            },
        },
        "phrases": {
            "windup": [
                "It scurries forward in a sudden burst — teeth first.",
                "The rat freezes, then launches itself at your leg.",
                "It moves along the ground faster than it has any right to.",
            ],
            "hit": [
                "Small teeth find the gap between your boot and your shin.",
                "It bites and holds on. You shake it free.",
                "A sharp pain — low down, easy to ignore until it isn't.",
            ],
            "miss": [
                "You stamp. It dodges. It has done this before.",
                "It misses and skitters past you into the dark.",
                "You kick out. It was already somewhere else.",
            ],
            "death": [
                "It stops. Just stops.",
                "A small thing. It was only hungry.",
                "It curls once and goes still.",
            ],
        },
    },

    "hermit": {
        "name":       "the Hermit",
        "name_short": "the Hermit",
        "hp":         45,
        "damage":     (7, 14),
        "accuracy":   0.62,
        "shards":     (50, 100),
        "loot":       [("dried herbs", 0.7), ("runic token", 0.3)],
        "variants": {
            "hostile": {
                "hp":       45,
                "damage":   (10, 18),
                "accuracy": 0.68,
                "weapon":   {"name": "iron staff", "effect": "bleeding"},
            },
            "mad": {
                "hp":       35,
                "damage":   (12, 22),
                "accuracy": 0.72,
            },
        },
        "phrases": {
            "windup": [
                "He moves without warning — faster than an old man should.",
                "He mutters something and swings the staff low.",
                "He stops talking and that is when you know it has started.",
            ],
            "hit": [
                "The staff catches your knee. He knows where it hurts.",
                "He is inside your guard before you see it. The blow lands clean.",
                "A sharp strike to the shoulder. He has done this before.",
            ],
            "miss": [
                "He overreaches. The years cost him something after all.",
                "You step back. He does not follow — he waits.",
                "The blow goes wide. He does not seem surprised.",
            ],
            "death": [
                "He sits down slowly, as if he chose it.",
                "He says something you don't catch. Then he is still.",
                "He looks almost relieved.",
            ],
        },
    },

    "draugar_weak": {
        "name":       "a Risen Footsoldier",
        "name_short": "the Draugar",
        "hp":         40,
        "damage":     (8, 16),
        "accuracy":   0.60,
        "shards":     (60, 120),
        "loot":       [("iron scraps", 0.7), ("echo dust", 0.9)],
        "variants": {
            "frenzied": {
                "hp":       65,
                "damage":   (12, 22),
                "accuracy": 0.70,
                "weapon":   {"name": "jagged axe", "effect": "bleeding"},
            },
        },
        "phrases": {
            "windup": [
                "It raises both rotting arms, a slow overhead swing telegraphed by its dead eyes.",
                "The thing lurches forward, arms wide — you can see the blow coming.",
                "It groans and swings wide, ice-slow.",
            ],
            "hit": [
                "The axe catches you across the ribs. Something cracks.",
                "You are too slow. The blow lands against your shoulder.",
                "It finds a gap in your guard. The pain is distant, numbed by something older than pain.",
            ],
            "miss": [
                "You step aside. The thing stumbles through its own momentum.",
                "It misses. The axe buries itself in the mud.",
                "You turn your body and the blow passes through air.",
            ],
            "death": [
                "It collapses without a sound. Whatever held it upright is gone.",
                "The Draugar falls. Blue-grey mist rises from where it lands.",
                "It drops to the mud. The eyes dim — they were never truly lit.",
            ],
        },
    },

    "shieldwall_draugar": {
        "name":       "a Shieldwall Draugar",
        "name_short": "the Shieldwall",
        "hp":         65,
        "damage":     (12, 20),
        "accuracy":   0.55,
        "shield":     True,
        "flanked":    False,
        "shards":     (100, 180),
        "loot":       [("iron scraps", 1.0), ("cracked shield", 0.5)],
        "variants": {
            "veteran": {
                "hp":       90,
                "damage":   (15, 26),
                "accuracy": 0.65,
            },
            "cornered": {
                "hp":       45,
                "damage":   (18, 30),
                "accuracy": 0.72,
                "weapon":   {"name": "desperation", "effect": "bleeding"},
            },
        },
        "phrases": {
            "windup": [
                "It bashes its shield forward and swings behind the momentum.",
                "The creature advances in a tight guard stance. It knows how to fight.",
                "It shouts — a broken, wet sound — and the Draugar nearby begin to stir.",
            ],
            "hit": [
                "You are caught. The iron rim of the shield hits first, then the blade.",
                "It punches through your guard. You taste iron.",
                "The blow is heavier than it should be. Your knees buckle.",
            ],
            "miss": [
                "You roll under the arc. The Shieldwall cannot stop its own momentum.",
                "You circle left. It cannot turn fast enough.",
                "The strike grazes you — close, too close.",
            ],
            "death": [
                "Without the shield raised, it was never a warrior. Just a body remembering war.",
                "It falls in pieces — the shield first, then it.",
                "The Shieldwall crumbles. The others nearby seem to notice.",
            ],
        },
    },

    "fog_sentinel": {
        "name":         "the Fog-Sentinel",
        "name_short":   "the Sentinel",
        "hp":           55,
        "damage":       (10, 22),
        "accuracy":     0.65,
        "drain":        True,
        "drain_amount": 8,
        "shards":       (80, 140),
        "loot":         [("fog shard", 1.0)],
        "variants": {
            "awakened": {
                "hp":           80,
                "damage":       (14, 28),
                "accuracy":     0.72,
                "drain_amount": 14,
            },
            "fractured": {
                "hp":           30,
                "damage":       (7, 16),
                "accuracy":     0.50,
                "drain_amount": 3,
            },
        },
        "phrases": {
            "windup": [
                "The bell-tone rises. Its arms extend toward you — not reaching, containing.",
                "It rotates toward you without moving its feet. The sound becomes pressure.",
                "The fog thickens around it. You feel the air trying to hold you still.",
            ],
            "hit": [
                "The contact is wrong — not pain exactly. More like something leaving you.",
                "It touches you and the bell-tone spikes. Your wrath drains with it.",
                "You are struck and for a moment you forget what you were angry about.",
            ],
            "miss": [
                "You step outside its reach. The sound follows but the arms do not.",
                "It passes through where you were. Cold. Very cold.",
                "You move. It recalibrates — slowly, like a compass finding north.",
            ],
            "drain_trigger": [
                "Your strike lands — and you feel it pull something back. The Sentinel steadies.",
                "It absorbs the blow. Not taking damage — taking fuel.",
                "The harder you hit, the more it drinks.",
            ],
            "death": [
                "The bell-tone stops. Not fades — stops. Mid-ring, like a thread cut.",
                "It collapses inward, not outward. As if it was always mostly absence.",
                "The fog where it stood is colder than the rest. For a long time after.",
            ],
        },
    },

    "gunnar": {
        "name":          "Gunnar the Hollow King",
        "name_short":    "Gunnar",
        "hp":            120,
        "damage":        (14, 28),
        "accuracy":      0.72,
        "phases":        3,
        "current_phase": 1,
        "shards":        (2400, 2400),
        "loot":          [],
        "on_death": {
            "memory": ("gunnar_defeated", "The death of Gunnar the Hollow King"),
        },
        "phrases": {
            "windup": [
                "Gunnar steps back — and for a moment you see the man he was. Then the axe rises.",
                '"You remember," he says. He swings.',
                "He shifts his weight. Every movement is something you were taught. By him.",
            ],
            "hit": [
                '"Still slow," he says, as the axe bites into your side.',
                "He catches you with the flat of the blade. Humiliating. Deliberate.",
                "You feel the blow before you see it. Muscle memory. His.",
            ],
            "miss": [
                "You remember this. You have drilled against this exact strike a hundred times.",
                "You parry — and for a moment, he looks almost proud.",
                "You step inside his reach. He was not expecting that. Neither were you.",
            ],
            "taunt": [
                '"You broke your oath. Odin does not forget."',
                '"I remember what you did. Do you?"',
                '"Fight me like you mean it. Fight me like that night."',
                '"Why do you think the Valkyries never came?"',
            ],
            "phase2": "Gunnar roars — a sound that is not grief, not rage, but something between them. The air around him darkens.",
            "phase3": "He speaks a word in Old Norse you do not recognise. His shadow splits. There are two of him now — one still, one moving.",
            "death":  '"It... does not matter," he says. "You will wake. And I will be here. I am always here."',
        },
    },
}

# ── Enemy roster ───────────────────────────────────────────────
# Key                  Variants
# ─────────────────────────────────────────────────────────────
# rat                  giant, plague, swarm
# wolf                 pack_leader, starved, dire, silver
# hermit               hostile, mad
# draugar_weak         frenzied
# shieldwall_draugar   veteran, cornered
# fog_sentinel         awakened, fractured
# gunnar               (boss — no variants)
