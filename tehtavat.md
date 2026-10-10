# Projektitehtävien toteutus

Tämä tiedosto yhdistää [kurssin harjoitussivun Projekti 1–5 -tehtävät](https://metropolia-sw.github.io/sw1-python/fi/tehtavat.html) tämän peliprojektin toteutukseen. Tarkistus perustuu lähdekoodiin 2.10.2026. Rivinumerot viittaavat tämänhetkisiin tiedostoihin.

**Toteutettu** tarkoittaa, että vaatimus löytyy koodista. **Osittain** tarkoittaa, että toteutuksessa on tehtävänantoon nähden puutteita. Palautusten ajankohtia tai projektin pisteytystä ei voi todentaa näistä tiedostoista.

## Projekti 1 – Ohjelmointiprojektitehtävän aloitus

| Vaatimus | Toteutuspaikka | Toteutus ja tila |
| --- | --- | --- |
| Oma `peliprojekti/`-kansio harjoitusprojektin sisällä. | Tämä kansio: `ohjelmisto1/peliprojekti/`. | **Toteutettu.** |
| README-tiedosto, jossa on pelin otsikko ja tekijän nimi. | [README.md](README.md#L1), rivit 1–3. | **Toteutettu.** Otsikkona on ”Terminaali tarinapeli-projekti” ja tekijänä Nikolaos Gavras. Tiedoston nimi on `README.md`, tehtävänannossa `readme.md`. |
| Pelaajan nimen ja iän kysyminen ja tallentaminen muuttujiin. | [main.py](main.py#L36), rivit 36–44. | **Toteutettu.** Uuden pelin alussa kysytään `age` ja `name`. Virheellinen ikäsyöte kysytään uudelleen. |
| Nimen ja iän tulostaminen konsoliin. | [main.py](main.py#L102), rivit 102–104; [nayta_tiedot.py](functions/nayta_tiedot.py#L1), rivit 1–5. | **Toteutettu `TIEDOT`-komennolla.** Aloituksen tervehdys tulostaa vain nimen (`main.py`, rivi 49); ikää ei tulosteta automaattisesti alussa. |

## Projekti 2 – Päävalikko

| Vaatimus | Toteutuspaikka | Toteutus ja tila |
| --- | --- | --- |
| Alle 12-vuotiaalle ilmoitetaan ikärajasta ja ohjelma suljetaan. | [main.py](main.py#L45), rivit 45–47. | **Toteutettu uuden pelin yhteydessä.** `age < 12` tulostaa ilmoituksen ja päättää ohjelman `SystemExit`-poikkeuksella. Tallennuksesta luettua ikää ei tarkisteta tässä haarassa. |
| Sallitun ikäinen pelaaja saa tervehdyksen. | [main.py](main.py#L49), rivi 49; ladattaessa rivi 30. | **Toteutettu.** Tervehdyksessä käytetään pelaajan nimeä. |
| Päävalikko tulostetaan alussa ja uudelleen jokaisen komennon jälkeen. | [main.py](main.py#L50), rivi 50 ja rivit 202–203; [nayta_ohje.py](functions/nayta_ohje.py#L1). | **Osittain.** Komentolista on olemassa, mutta se näytetään vain `HELP`-komennolla. Alussa tulostetaan kehotus käyttää `help`-komentoa; komentolista ei toistu automaattisesti. |
| Komentoja kysytään toistuvasti, kunnes pelaaja kirjoittaa `lopeta`. | [main.py](main.py#L97), rivit 97–101; [lopeta_peli.py](functions/lopeta_peli.py#L1). | **Toteutettu.** `while True` kysyy komentoja, ja `LOPETA` tai `QUIT` sulkee pelin. Syöte muutetaan isoiksi kirjaimiksi, joten myös `lopeta` toimii. |
| Useita komentoja, joilla on erilaiset tulosteet. | [main.py](main.py#L102), rivit 102–142 ja 189–203. | **Toteutettu.** Esimerkiksi `TIEDOT`, `REPPU`, `LIIKU`, `ETSI`, `POISTA` ja `HELP` tekevät eri asioita. |

## Projekti 3 – Päävalikon toiminnot ja inventaario

| Vaatimus | Toteutuspaikka | Toteutus ja tila |
| --- | --- | --- |
| Jokaisella päävalikon toiminnolla on oma funktio; toimintoja on vähintään kolme. | [main.py](main.py#L4), tuonnit riveillä 4–8; [functions/](functions/). | **Osittain.** Viidelle toiminnolle on omat funktiot: `lopeta_peli`, `nayta_tiedot`, `nayta_inventaario`, `poista_esine` ja `nayta_ohje`. `LIIKU`-, `ETSI`-, `KORJAA`- ja `TALLENNA`-komentojen käsittely on kuitenkin pääohjelman `match`-rakenteessa. Liikkuminen käyttää lisäksi pelaajan metodia. |
| Yksi funktio kysyy käyttäjältä lisättäviä asioita ja lisää ne listaan. | [main.py](main.py#L128), rivit 128–142. | **Osittain.** `ETSI` kysyy, otetaanko löydetty esine mukaan, ja lisää hyväksytyn esineen `pelaaja.player_items`-listaan. Kysymistä ja lisäämistä ei ole erotettu omaksi funktioksi. |
| Toinen funktio tulostaa listan sisällön. | [nayta_inventaario.py](functions/nayta_inventaario.py#L1), rivit 1–10; kutsu [main.py](main.py#L105), rivit 105–106. | **Toteutettu.** `REPPU` / `INVENTAARIO` näyttää esineiden nimet numeroituina `for`-silmukalla tai ilmoittaa tyhjästä repusta. |
| Muut toiminnot voidaan suunnitella vapaasti. | [poista_esine.py](functions/poista_esine.py#L1), [nayta_tiedot.py](functions/nayta_tiedot.py#L1), [lopeta_peli.py](functions/lopeta_peli.py#L1). | **Toteutettu.** Esineen voi poistaa nimellä tai numerolla, pelaajan tiedot voi näyttää ja pelin voi lopettaa. |

## Projekti 4 – Rakenne kuntoon ja oliot käyttöön

Tehtävänannon luokkarakenne on esimerkkimalli. Tässä projektissa luokkien nimet ovat englanniksi: `Player`, `Room` ja `Item`.

| Vaatimus | Toteutuspaikka | Toteutus ja tila |
| --- | --- | --- |
| Ohjelma jaetaan moduuleihin ja paketteihin, ja rakenne kuvataan README-tiedostossa. | [main.py](main.py#L1), rivit 1–8; [classes/](classes/), [functions/](functions/); [README.md](README.md), kohta ”Tiedosto- ja moduulirakenne”. | **Toteutettu.** Pääohjelma tuo luokat ja apufunktiot erillisistä moduuleista. Hakemistot toimivat Pythonin nimiavaruuspaketteina ilman `__init__.py`-tiedostoja. |
| Esineluokalla on esimerkiksi nimi ja paino. | [item.py](classes/item.py#L1), rivit 1–4. | **Toteutettu.** `Item.__init__` asettaa ominaisuudet `item_name` ja `item_weight`. |
| Pelaajalla on nimi, esinelista ja nykyinen huone. | [player.py](classes/player.py#L1), rivit 1–5. | **Toteutettu.** `player_name`, `player_items` ja `player_location`; sijainti viittaa `Room`-olioon ja reppu sisältää `Item`-olioita. |
| Huoneella on nimi ja mahdollisesti esine. | [room.py](classes/room.py#L5), rivit 5–12 ja 14–27. | **Toteutettu.** `Room` sisältää nimen, kuvauksen ja `items`-listan. Huoneessa voi olla useita esineitä; luonti voi lisätä satunnaisen esineen. |
| Käynnistyksessä luodaan pelaaja sekä useita huoneita ja esineitä. | [main.py](main.py#L60), rivit 60–87. | **Toteutettu.** Luodaan viisi huonetta, viisi tarinan esinettä ja yksi pelaaja. Tarinan esineet sijoitetaan huoneiden listoihin. |
| Pelaaja voi liikkua valikon kautta. | [main.py](main.py#L107), rivit 107–127; [player.py](classes/player.py#L11), rivit 11–12. | **Toteutettu.** `LIIKU` kysyy kohdehuoneen ja kutsuu `Player.move_to_room`-metodia. |
| Pelaaja voi kerätä esineitä valikon kautta. | [main.py](main.py#L128), rivit 128–142; [player.py](classes/player.py#L8), rivit 8–10. | **Toiminto toteutettu, luokan metodi puutteellinen.** `ETSI` siirtää esineen huoneen listasta pelaajan listaan suoraan pääohjelmassa. `Player.take_item` on olemassa mutta käyttämätön; se kutsuu puuttuvaa `Room.remove_item`-metodia ja aiheuttaisi kutsuttaessa virheen. |
| Valikossa näkyvät liikkuminen ja esineen kerääminen. | [nayta_ohje.py](functions/nayta_ohje.py#L4), rivit 4–5. | **Toteutettu.** `HELP` luettelee `LIIKU`- ja `ETSI`-komennot. |

Olioiden assosiaatiot näkyvät pelaajan huoneviitteessä sekä pelaajan ja huoneiden esinelistoissa. Käytössä oleva liikkumismetodi on `move_to_room`; erillistä `Player.move`-metodia ei kutsuta pelissä.

## Projekti 5 – Tiedostonkäsittely

| Vaatimus | Toteutuspaikka | Toteutus ja tila |
| --- | --- | --- |
| Esittely ja ohjeet luetaan erillisistä tekstitiedostoista ja tulostetaan käynnistyksessä. | [main.py](main.py#L52), rivit 52–58; [intro.txt](intro.txt), [instructions.txt](instructions.txt). | **Toteutettu.** Molemmat tiedostot luetaan `with open(..., "r")` -rakenteella ja tulostetaan. Ohjetiedoston nimi on `instructions.txt`; tehtävänannon tiedostonimet ovat esimerkkejä. |
| Pelitilanne tallennetaan tekstitiedostoon. | [main.py](main.py#L194), rivit 194–201; [save.json](save.json). | **Osittain.** `TALLENNA` kirjoittaa nimen, iän, nykyisen huoneen ja repun esineiden nimet. Huoneiden esinetilannetta ja esineiden painoja ei tallenneta. |
| Tallennettua peliä voi jatkaa käynnistyksen yhteydessä siitä, mihin jäi. | [main.py](main.py#L19), rivit 19–34 ja 89–95. | **Osittain.** Käynnistys kysyy lataamisesta ja palauttaa tallennetut pelaajatiedot, huoneen ja repun nimet. Huoneet ja niiden esineet luodaan uudelleen, joten koko pelimaailman aiempi tila ei palaudu. |

Tallennuksen nykyiset rajaukset:

- Jo kerätyt tarinaesineet ilmestyvät latauksessa uudelleen huoneisiin (`main.py`, rivit 75–85), ja huoneiden satunnaisesineet arvotaan uudelleen (`classes/room.py`, rivit 11–12).
- Repun esineistä luodaan latauksessa uudet `Item`-oliot, joiden painoksi asetetaan aina `1.0` (`main.py`, rivi 93).
- Tallennuskomento toimii, mutta se puuttuu `HELP`-komentolistasta (`functions/nayta_ohje.py`).

## Tehtävänantoihin nähden jäljellä olevat kohdat

1. Näytä päävalikon komentolista alussa ja jokaisen komennon jälkeen (Projekti 2).
2. Siirrä jokaisen päävalikon toiminnon käsittely omaan funktioonsa; erityisesti esineen ottamista kysyvä ja listaan lisäävä toiminto (Projekti 3).
3. Korjaa `Player.take_item` ja kytke kerääminen siihen, jotta myös pelaajaluokan keräämismetodi toimii (Projekti 4:n oliomalli).
4. Tallenna ja palauta myös huoneiden esineet ja esineiden ominaisuudet, jotta jatkaminen säilyttää koko pelitilanteen (Projekti 5).

Dokumentti kuvaa nykyisen toteutuksen. Se ei muuta pelin toimintaa.
