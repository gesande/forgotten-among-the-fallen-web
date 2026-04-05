# TODO — Forgotten Among the Fallen

## Content

- [x] **Act III** — avauskohtaus (firepit + avainmuisto), Tyr-temppeli täysin kirjoitettu (lähestyminen, tarjoaminen, dialogi, tuomio, lähtö); loppuu `act3_the_memory` placeholderiin
- [ ] **Act III jatko** — `act3_the_memory` ja sen jälkeiset kohtaukset (Odinin kohtaaminen, avainmuisto tienristeyksestä, kolme loppua)
- [ ] **Act IV** — suunniteltu, ei aloitettu
- [x] **name_entry** — art lisätty

## Gameplay

- [x] **Mercy-mekaniikka** — wolf mercy path (mercy>=10): dire wolf passes without fight; hermit_mercy scene (mercy>=10); hermit_greet honour variant (honour>=65); hermit opening adapts to wolf_killed/wolf_spared/neither
- [ ] **Runic Burst** — echo shards -systeemi toimii, lisää käyttötilanteita?
- [ ] **Curse stacks** — maksimi 5, mutta vaikutus loppupelissä voisi kasvaa
- [x] **Rune stone** — `forest_rune_stone` hub Act II metsässä; susi/karhu/hermit rinnakkaisina reitteinä; heal kerran

## Combat

- [ ] **Corpse art** — taistelun lopuksi näytetään vihollisen corpse-kuva ennen siirtymää
- [x] **Heavy strike kasvattaa brutalitya** — heavy hit +3, killing blow +5 lisää
- [x] **Killing blow vaikuttaa statseihin** — heavy killing blow +5 brutality
- [x] **Resolve taistelussa** — near-death (HP < 20%) -8 resolve kerran per taistelu; boss phase transition -6 resolve
- [x] **Karhu-vihollinen** — `bear` + `berserker`-variantti lisätty; `forest_bear`-kohtaus Act II metsässä
- [x] **Suden/karhun nahat** — `wolf pelt` / `bear pelt` body-slot; bear pelt aktivoi berserk-moodin
- [x] **Odin-muistot** — kaksi muistoa per eläin: ensimmäinen näky + tapon jälkeen
- [x] **Battlefield wolf** — pack_leader-variantti, `combat_wolf_battlefield`-kohtaus ja art

## Engine

- [ ] **`state.py` geneerinen** — defaultit duplikaatteina `state.py`:ssä ja `STATS`-dictissä; täysi data-driven vaatisi `stats`-dictiä `PlayerState`ssa. Kustannus (syntaksi, save-yhteensopivuus) ylittää hyödyn tässä pelissä — jätä jos engine joskus irrotetaan omaksi kirjastoksi.
- [x] **Combat-kynnykset configiin** — kaikki numerot `COMBAT_CONFIG`-dictiin `game_config.py`:ssä
- [ ] **`engine/moral.py`** — eristä loppujen logiikka omaan tiedostoon (`resolve_ending`, `moral_profile`) kun Act III loppukohtaukset on kirjoitettu; turha ennen sitä

## Polish

- [ ] **Mobiili** — responsiivinen layout olemassa, testaamatta kunnolla
- [x] **Save/load UI** — "✦ saved" -indikaattori HUD:ssa 2s jokaisen autosaven jälkeen
- [ ] **Credits** — Act I complete -teksti, lisää sisältöä?

## Tunnetut bugit

- [x] **Vihollisen healthbar** jää näkyviin taistelun jälkeen
- [x] ~~Shieldwall draugar -taistelun häviön jälkeen ei pääse yrittämään uudelleen~~ — tarkoituksellinen
- [x] **Sentinel flee** — Odrik sanoo "You fought the Sentinel" vaikka pelaaja väisti/pakeni
