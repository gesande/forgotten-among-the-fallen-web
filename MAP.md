# MAP — Forgotten Among the Fallen

## Act I — The Battlefield of Silence

```
name_entry
  └─ awakening
       ├─ find_weapon ──────────────────────────────┐
       └─ battlefield_open ◄────────────────────────┘
            │
            ├─ [!leif_done] soul_leif
            │       ├─ leif_battle_account
            │       │     └─ leif_gives_name
            │       │           ├─ leif_the_oath
            │       │           │     └─ leif_gunnar_intro
            │       │           │           └─ leif_farewell
            │       │           │                 └─ leif_knife_offer
            │       │           │                       ├─ leif_knife_taken ──┐
            │       │           │                       └─ leif_ambush ◄──────┘
            │       │                                         └─ combat_shieldwall_leif
            │       │                                               └─ battlefield_open
            │       └─ leif_mercy_kill
            │             └─ leif_ambush (see above)
            │
            ├─ [!found_forge] longhouse_ruins
            │       ├─ cairn_rest ──────────────────┐
            │       ├─ longhouse_embers ─────────────┤
            │       ├─ forge_search                  │
            │       └─ forge_sharpen                 │
            │             └─ longhouse_ruins ────────┘
            │                                        └─ battlefield_open
            │
            ├─ [!east_searched] scavenge_east
            │       └─ combat_draugar_east
            │             └─ scavenge_east_after ──► battlefield_open
            │
            ├─ [east_searched & !defeated_wolf_battlefield] scavenge_east_return
            │       └─ combat_wolf_battlefield ──────► battlefield_open
            │
            ├─ [found_forge | east_searched] the_mound
            │       ├─ gunnar_dialogue_peace ─────┐
            │       ├─ gunnar_dialogue_challenge ──┤
            │       └─ gunnar_dialogue_truth ──────┘
            │                                      └─ combat_gunnar
            │                                            └─ act1_end
            │                                                  ├─ final_rest
            │                                                  │     └─ act_2_intro
            │                                                  └─ act_2_intro
            │
            └─ battlefield_look_around ──────────────► battlefield_open
```

## Act II — The Fog Road

```
act_2_intro
  └─ fog_road
       ├─ fog_the_held
       │     ├─ fog_held_other ──────────┐
       │     ├─ fog_held_release ─────────┤
       │     └─ fog_held_after ◄──────────┘
       │           └─ fog_sentinel
       │
       └─ [forest detour] forest_path
             ├─ forest_wolf
             │     ├─ forest_bear ──────────────┐
             │     └─ hermit_oak ◄──────────────┘
             │           ├─ hermit_greet
             │           │     ├─ hermit_battlefield
             │           │     ├─ hermit_silence
             │           │     ├─ hermit_who
             │           │     │     └─ hermit_why
             │           │     └─ hermit_oath
             │           │           └─ hermit_depart
             │           └─ fog_sentinel (skip hermit)
             │
             └─ fog_road (turn back)

fog_sentinel
  ├─ fog_sentinel_wait
  │     ├─ combat_fog_sentinel ──────┐
  │     └─ fog_sentinel_avoided ─────┤
  ├─ combat_fog_sentinel             │
  └─ fog_sentinel_avoided            │
        └─ fog_sentinel_after ◄──────┘
              └─ gatehouse_approach
                    ├─ gatehouse_guards_hostile
                    │     ├─ gatehouse_guards_calmed ─┐
                    │     ├─ gatehouse_guards_spoken ──┤
                    │     ├─ gatehouse_guards_axe ─────┤
                    │     └─ gatehouse_guards_forced ──┤
                    ├─ gatehouse_guards ───────────────┤
                    ├─ gatehouse_courtyard ────────────┤
                    └─ gatehouse_wall ─────────────────┘
                                                       └─ gatehouse_inside
                                                             └─ great_hall_entrance
                                                                   │
                                                             [Odrik dialogue hub]
                                                             odrik_silence
                                                             odrik_knows
                                                             odrik_what_are_you
                                                             odrik_measures_you
                                                               └─ odrik_first_questions
                                                                     ├─ odrik_explains_place
                                                                     ├─ odrik_the_night
                                                                     ├─ odrik_the_key
                                                                     ├─ odrik_why_bound
                                                                     └─ odrik_go_forward
                                                                           └─ act2_end
                                                                                 └─ act_3_intro
```

## Act III — (placeholder)
## Act IV — (planned)

---

## Combat encounters

| Key | Enemy | Variant | Location |
|-----|-------|---------|----------|
| combat_shieldwall_leif | draugar_weak | shieldwall | Act I — Leif ambush |
| combat_draugar_east | draugar_weak | — | Act I — Dense dead |
| combat_wolf_battlefield | wolf | pack_leader | Act I — Dense dead return |
| combat_gunnar | gunnar | — | Act I — The Mound |
| combat_fog_sentinel | fog_sentinel | — | Act II — Fog road |
| forest_wolf | wolf | dire | Act II — Dark wood |
| forest_bear | bear | berserker | Act II — Dark wood (deeper) |

## Key flags

| Flag | Set by | Guards |
|------|--------|--------|
| `leif_done` | leif_ambush | Leif choices, the_mound access |
| `found_forge` | forge_search | the_mound access, look_around choices |
| `east_searched` | scavenge_east | scavenge return, look_around choices |
| `defeated_wolf_battlefield` | combat_wolf_battlefield | hides scavenge return choice |
| `sentinel_avoided` | fog_sentinel_avoided | Odrik dialogue variant |
| `defeated_fog_sentinel` | combat_fog_sentinel | Odrik dialogue variant |
| `held_released` | fog_held_release | gatehouse approach prose variant |
| `held_forced` | fog_held_after | gatehouse approach prose variant |
