import random


def nayta_inventaario(tavarat):
    if not tavarat:
        print("Reppusi on tyhjä.")
    else:
        print("\n--- REPUN SISÄLTÖ ---")
        numero = 1
        for tavara in tavarat:
            print(f"{numero}. {tavara}")
            numero += 1
        print("--------------------")


def lisaa_esine(tavarat):
    esine = input("Minkä esineen haluat lisätä reppuun?: ").strip()
    if esine:
        tavarat.append(esine)
        print(f"Esine {esine} lisättiin reppuusi.")
    else:
        print("Et syöttänyt esineen nimeä, mitään ei lisätty.")


def poista_esine(tavarat):
    if not tavarat:
        print("Reppusi on jo tyhjä, mitään ei voi poistaa.")
        return

    print("\nRepussasi on tällä hetkellä:")
    numero = 1
    for tavara in tavarat:
        print(f"{numero}. {tavara}")
        numero += 1

    poistettava = input("Minkä esineen haluat poistaa (nimi tai numero)? ").strip()

    if poistettava.isdigit():
        numero = int(poistettava)
        if 1 <= numero <= len(tavarat):
            poistettu = tavarat.pop(numero - 1)
            print(f"Esine '{poistettu}' poistettiin repusta.")
            return
        else:
            print("Virheellinen numero.")
            return

    loytynyt = None
    for tavara in tavarat:
        if tavara.lower() == poistettava.lower():
            loytynyt = tavara
            break

    if loytynyt:
        tavarat.remove(loytynyt)
        print(f"Esine '{loytynyt}' poistettiin repusta.")
    else:
        print(f"Esinettä '{poistettava}' ei löytynyt repustasi.")


def tutki_ymparistoa(tavarat):
    loydot = ["Taskulamppu", "Vanha avain", "Karttapala", "Pieni parannusjuoma", "Kultakolikko", "Kompassi"]
    loydetty = random.choice(loydot)
    print(f"\nTutkit ympäröivää maastoa ja huomaat jotain kiinnostavaa...")
    print(f"Löysit esineen: {loydetty}!")
    valinta = input("Haluatko poimia sen reppuusi? (y/n): ").strip().lower()
    if valinta in ("k", "kylla", "kyllä", "yes", "y"):
        tavarat.append(loydetty)
        print(f"Poimit esineen '{loydetty}' reppuusi.")
    else:
        print(f"Päätit jättää esineen '{loydetty}' maahan.")


def nayta_tiedot(pelaajan_nimi, pelaajan_ika, tavarat):
    print(f"\n--- PELAAJAN TIEDOT ---")
    print(f"Nimi: {pelaajan_nimi}")
    print(f"Olet {pelaajan_ika} vuotta vanha.")
    print(f"Esineitä repussa: {len(tavarat)} kpl")


def arvo_sana():
    sanat = ["Viikko", "Pöytä", "Pannu", "Juomalasi", "Lompakko", "Miekka", "Seikkailu"]
    valittu = random.choice(sanat)
    print(f"Satunnainen sana: {valittu}")


def nayta_ohje():
    #Tulostaa listan kaikista käytettävissä olevista komennoista.
    print("\n--- KOMENNOT ---")
    print("REPPU (tai INVENTAARIO) - Näytä repun sisältö")
    print("LISÄÄ                   - Lisää itse uusi esine reppuun")
    print("POISTA                  - Poista esine repusta")
    print("TUTKI                   - Tutki ympäristöä ja etsi esineitä")
    print("TIEDOT (tai IKÄ)        - Näytä pelaajan tiedot ja ikä")
    print("RANDOMSANA              - Arvo satunnainen sana")
    print("HELP (tai OHJE)         - Näytä tämä komentolista")
    print("LOPETA                  - Sulje peli")


def lopeta_peli():
    """Sulkee pelin."""
    print("Suljetaan ohjelma. Kiitos pelaamisesta!")
    raise SystemExit


while True:
    try:
        age = int(input("Syötä ikäsi: "))
        break
    except ValueError:
        print("Syötä numero")

name = str(input("Syötä nimesi: "))
if age < 12:
    print("Käyttäjän ikä on liian alhainen. Ohjelma suljetaan.")
    raise SystemExit

print(f"\nTervetuloa {name}!")
print("Voit kirjoittaa 'help' nähdäksesi kaikki komennot.")

inventaario = []

while True:
    userCommandInput = input("\nSyötä komento: ").upper().strip()
    match userCommandInput:
        case "LOPETA":
            lopeta_peli()
        case "IKÄ" | "TIEDOT":
            nayta_tiedot(name, age, inventaario)
        case "REPPU" | "INVENTAARIO":
            nayta_inventaario(inventaario)
        case "LISÄÄ" | "LISAA":
            lisaa_esine(inventaario)
        case "POISTA":
            poista_esine(inventaario)
        case "TUTKI":
            tutki_ymparistoa(inventaario)
        case "RANDOMSANA":
            arvo_sana()
        case "HELP" | "OHJE":
            nayta_ohje()
        case _:
            print("Tuntematon komento, yritä uudelleen, voit myös kirjoittaa 'help' komentoriviin nähdäksesi kaikki komennot.")
