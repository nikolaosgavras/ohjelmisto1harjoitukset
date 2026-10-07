## Projekti 1: tehty

- `main.py`, rivit 45–56: kysytään uuden pelaajan ikä ja nimi ja tallennetaan ne muuttujiin. Virheellinen ikäsyöte kysytään uudelleen.
- `main.py`, rivit 58–59 ja `functions/nayta_tiedot.py`, rivit 1–5: tulostetaan nimi ja ikä käynnistyksessä sekä `TIEDOT`-komennolla.

## Projekti 2: tehty

- `main.py`, rivit 53–58: alle 12-vuotiaan uusi peli suljetaan, muut saavat tervehdyksen.
- `functions/load_save.py`, rivit 50–62: myös tallennuksesta ladatun pelaajan ikä tarkistetaan. Alle 12-vuotiaan tallennusta ei hyväksytä.
- `main.py`, rivit 72–77: valikko näytetään ennen jokaista komentoa, kunnes pelaaja lopettaa komennolla `LOPETA` tai `QUIT`.
- `functions/nayta_ohje.py`, rivit 1–12: valikon komennot ja niiden kuvaukset, mukaan lukien `TALLENNA`.
- `main.py`, rivit 74–96: esimerkiksi `TIEDOT`, `REPPU`, `LIIKU` ja `ETSI` tekevät eri asioita. Komennot hyväksytään myös pienillä kirjaimilla.

## Projekti 3: tehty

- `main.py`, rivit 5–14: tuodaan kymmenen omaa apufunktiota. Jokaiselle valikon toiminnolle on oma funktio, jota kutsutaan komentojen käsittelyssä (rivit 75–94).
- `functions/etsi.py`, rivit 1–15: kysytään esineen ottamisesta ja siirretään hyväksytty esine huoneesta reppuun pelaajan metodilla.
- `functions/nayta_inventaario.py`, rivit 1–10: tulostetaan repun sisältö numeroituna tai ilmoitetaan tyhjästä repusta.
- `functions/poista_esine.py`, rivit 1–33: poistetaan esine nimellä tai numerolla.
- `functions/liiku.py`, rivit 1–21: kysytään kohdehuone ja siirretään pelaaja sinne.
- `functions/korjaa.py`, rivit 4–48: käsitellään aurinko-, tuuli- ja maalämpöreittien korjaaminen.
- `functions/tallenna_peli.py`, rivit 4–19: tallennetaan pelitilanne. `functions/load_save.py`, rivit 8–62: kysytään ja ladataan tallennus käynnistyksessä.

## Projekti 4: tehty

- `main.py`, rivit 1–14: pääohjelma käyttää `classes/`-kansion luokkia ja `functions/`-kansion apufunktioita. Moduulirakenne kuvataan `README.md`:ssä.
- `classes/item.py`, rivit 1–4: esineen nimi ja paino.
- `classes/player.py`, rivit 1–5: pelaajan nimi, reppu ja huone.
- `classes/room.py`, rivit 5–12 ja 17–30: huoneen nimi, kuvaus ja esinelista sekä satunnaisen esineen luominen.
- `main.py`, rivit 16–41 ja 56: luodaan viisi huonetta, viisi tarinaan liittyvää esinettä ja uuden pelin pelaaja sekä sijoitetaan esineet huoneisiin.
- `classes/player.py`, rivit 11–12 ja `functions/liiku.py`, rivit 11–19: pelaajan liikkuminen `LIIKU`-komennolla.
- `classes/player.py`, rivit 8–10 ja `classes/room.py`, rivit 14–15: toimiva `Player.take_item` poistaa esineen huoneesta ja lisää sen reppuun. `ETSI` käyttää tätä metodia (`functions/etsi.py`, rivit 8–11).

## Projekti 5: tehty

- `main.py`, rivit 62–66: luetaan ja tulostetaan `intro.txt` ja `instructions.txt` UTF-8-merkistöllä. Polut toimivat myös toisesta hakemistosta käynnistettäessä.
- `main.py`, rivit 91–92 ja `functions/tallenna_peli.py`, rivit 4–19: `TALLENNA` kirjoittaa pelitilanteen JSON-muotoisena tekstinä tiedostoon `save.txt`.
- Tallennukseen kuuluvat pelaajan nimi, ikä ja sijainti sekä repun ja kaikkien huoneiden esineet nimineen ja painoineen. Myös tyhjät huoneet säilyvät tyhjinä.
- `functions/load_save.py`, rivit 15–57: palautetaan pelaaja ja huoneiden esinetilanne. Kerätyt esineet eivät ilmesty uudelleen huoneisiin eikä tallennuksen satunnaisesineitä arvota uudelleen.
- `main.py`, rivit 43–44 ja 68–70: jatketaan ladatun pelaajan sijainnista ja näytetään palautunut reppu.
- `functions/load_save.py`, rivit 58–62: puuttuva tai virheellinen tallennus johtaa uuden pelin aloittamiseen. Huoneiden tilaa muutetaan vasta onnistuneen latauksen jälkeen.