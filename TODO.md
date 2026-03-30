# TODO — Forgotten Among the Fallen

## Content

- [ ] **Act III** — placeholder exists (`act_3_intro`), sisältö kirjoittamatta
- [ ] **Act IV** — suunniteltu, ei aloitettu
- [x] **name_entry** — art lisätty

## Gameplay

- [x] **Mercy-mekaniikka** — wolf mercy path (mercy>=10): dire wolf passes without fight; hermit_mercy scene (mercy>=10); hermit_greet honour variant (honour>=65); hermit opening adapts to wolf_killed/wolf_spared/neither
- [ ] **Runic Burst** — echo shards -systeemi toimii, lisää käyttötilanteita?
- [ ] **Curse stacks** — maksimi 5, mutta vaikutus loppupelissä voisi kasvaa
- [x] **Rune stone** — `forest_rune_stone` hub Act II metsässä; susi/karhu/hermit rinnakkaisina reitteinä; heal kerran

## Combat

- [ ] **Corpse art** — taistelun lopuksi näytetään vihollisen corpse-kuva ennen siirtymää
- [x] **Karhu-vihollinen** — `bear` + `berserker`-variantti lisätty; `forest_bear`-kohtaus Act II metsässä
- [x] **Suden/karhun nahat** — `wolf pelt` / `bear pelt` body-slot; bear pelt aktivoi berserk-moodin
- [x] **Odin-muistot** — kaksi muistoa per eläin: ensimmäinen näky + tapon jälkeen
- [x] **Battlefield wolf** — pack_leader-variantti, `combat_wolf_battlefield`-kohtaus ja art

## Engine

- [ ] **`state.py` geneerinen** — `PlayerState` tuntee stat-nimet suoraan (`wrath`, `honour` jne.); `is_cursed()` / `is_broken()` pelikohtaisia. Täysi data-driven vaatisi geneerisen stat-dictin.
- [ ] **Combat-kynnykset configiin** — `honour >= 40` (mercy), `echo_shards >= 100` (runic), wrath-gain arvot (10/18/25/8) kovakoodattu `combat.py`:ssä

## Polish

- [ ] **Mobiili** — responsiivinen layout olemassa, testaamatta kunnolla
- [x] **Save/load UI** — "✦ saved" -indikaattori HUD:ssa 2s jokaisen autosaven jälkeen
- [ ] **Credits** — Act I complete -teksti, lisää sisältöä?

## Tunnetut bugit

- [x] **Vihollisen healthbar** jää näkyviin taistelun jälkeen
- [x] ~~Shieldwall draugar -taistelun häviön jälkeen ei pääse yrittämään uudelleen~~ — tarkoituksellinen
- [x] **Sentinel flee** — Odrik sanoo "You fought the Sentinel" vaikka pelaaja väisti/pakeni
