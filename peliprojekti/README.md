# Terminaali tarinapeli-projekti

Nikolaos Gavras  



Peli ottaa suoraan kantaa YK:n kestävän kehityksen tavoitteeseen 7: Edullista ja puhdasta energiaa (Affordable and Clean Energy):
- Pelissä hylätään saastuttava ja rikkoutunut fossiilinen dieselgeneraattori.
- Aseman pelastus perustuu kokonaan uusiutuvien ja puhtaiden energiamuotojen käyttöönottoon.
- Pelaaja voi ratkaista energiakriisin valitsemalla minkä tahansa kolmesta vihreän energian ratkaisusta: aurinkoenergian, tuulivoiman tai geotermisen maalämmön.

## Kolme erilaista ratkaisureittiä (3 Winning Routes)

Pelin voi läpäistä vähintään kolmella toisistaan riippumattomalla tavalla:

1. **Reitti 1 – Aurinkoenergia (Kattotasanne):**
   * Etsi `Jakoavain` (Tuulikallio) ja `Aurinkokenno` (Kellari).
   * Siirry huoneeseen `KATTO` komennolla `LIIKU`.
   * Kirjoita `KORJAA` asentaaksesi uuden kennon ja ladataksesi aurinkoenergia-akut.

2. **Reitti 2 – Tuulivoimala (Tuulikallio):**
   * Etsi `Kiipeilyvaljaat` (Aula) ja `Voiteluöljy` (Katto).
   * Siirry huoneeseen `TUULIKALLIO` komennolla `LIIKU`.
   * Kirjoita `KORJAA` kiivetäksesi turbiiniin ja voidellaksesi jäätyneen akselin.

3. **Reitti 3 – Geoterminen maalämpö (Kellari):**
   * Etsi `Venttiiliavain` (Työpaja).
   * Siirry huoneeseen `KELLARI` komennolla `LIIKU`.
   * Kirjoita `KORJAA` ja syötä maalämpöpumpun oikea painelukema (`150` bar) avataksesi höyrykierron.

---

## Pelaaminen ja komennot

Peli käynnistetään komennolla:
```bash
python main.py
```

### Käynnistys ja tallennus:
* **Jatka peliä:** Ohjelman käynnistyessä peli kysyy suoraan, haluatko ladata aiemman tallennuksen (`save.txt`). Jos lataat, aiemmin syötetty nimi, ikä, huone ja reppu palautuvat automaattisesti.
* **Uusi peli:** Kysyy pelaajan iän (ikäraja K-12: alle 12-vuotiaat eivät pääse peliin) ja nimen.
* **Tarinan alustus:** Peli lukee alustuksen ja tehtävänannon suoraan ulkoisista tiedostoista `intro.txt` ja `instructions.txt`.

### Käytettävissä olevat komennot:
- Komennot löytyvät pelistä kirjoittamalla `help`.

### Tiedosto- ja moduulirakenne:
```text
peliprojekti/
├── README.md              # Projektin dokumentaatio
├── project.html           # Visuaalinen opas ja edistymisseuranta
├── intro.txt              # Tarinan taustatarina ja alkuteksti (luetaan koodissa)
├── instructions.txt       # Pelin tavoite ja tehtävänanto (luetaan koodissa)
├── save.txt               # Tallennustiedosto (luodaan automaattisesti tallennettaessa)
├── main.py                # Pääohjelma, pelisilmukka ja komentojen käsittely
│
├── classes/               # Olio-ohjelmoinnin luokat
│   ├── item.py            # Item-luokka (item_name, item_weight)
│   ├── player.py          # Player-luokka (nimi, sijainti, reppu, liikkuminen, esineiden poiminta)
│   └── room.py            # Room-luokka (huoneen nimi, kuvaus, esinelista ja satunnaisesineiden generointi)
│
└── functions/             # Modulaariset apufunktiot
    ├── lopeta_peli.py     # Pelin sulkemisfunktio
    ├── nayta_inventaario.py # Repun sisällön tulostus
    ├── nayta_ohje.py      # Komentolistauksen tulostus
    ├── nayta_tiedot.py    # Pelaajan tietojen tulostus
    └── poista_esine.py    # Esineen poisto repusta
```

### Olio-ohjelmointi:
Item luokka: Mallintaa esineitä (nimi ja paino).
Room luokka: Mallintaa tutkimusaseman tiloja, pitää kirjaa huoneen kuvauksesta ja huoneessa olevista esineistä.
Player luokka: Mallintaa pelaajaa, jolla on assosiaatiosuhteet nykyiseen Room-olioon ja repussa oleviin Item-olioihin.