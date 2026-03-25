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
#    shield      — enemy has a shield; damage +5/+8 until flanked
#    drain       — hits drain player wrath and partially heal enemy
#    drain_amount — wrath drained per hit (default 0)
#    phases      — boss phase count (int); enables phase transitions
# ============================================================

ENEMIES = {
    "draugar_weak": {
        "name":       "a Risen Footsoldier",
        "name_short": "the Draugar",
        "hp":         40,
        "damage":     (8, 16),
        "accuracy":   0.60,
        "shards":     (60, 120),
        "loot":       [("iron scraps", 0.7), ("echo dust", 0.9)],
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
