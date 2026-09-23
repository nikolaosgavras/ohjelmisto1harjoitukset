import random
from classes import player, room, item
from functions.lopeta_peli import lopeta_peli
from functions.nayta_ohje import nayta_ohje

def nayta_inventaario(tavarat):
    if not tavarat:
        print("Reppusi on tyhjä.")
    else:
        print("\n--- REPUN SISÄLTÖ ---")
        numero = 1
        for tavara in tavarat:
            print(f"{numero}. {tavara.item_name}")
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

testiEsine1 = item.Item("Test 1", 20.00)
testiEsine2 = item.Item("Jakoavain", 50.35)
testiEsine3 = item.Item("Vasara", 531.63)

aula = room.Room("Aula")
tyopaja = room.Room("Työpaja")
katto = room.Room("Katto")

huoneet = {
    "AULA": aula,
    "TYÖPAJA": tyopaja,
    "KATTO": katto,
}

pelaaja = player.Player(name, [], aula)

while True:
    userCommandInput = input("\nSyötä komento: ").upper().strip()
    match userCommandInput:
        case "LOPETA" | "QUIT":
            lopeta_peli()
        case "TIEDOT":
            nayta_tiedot(name, age, pelaaja.player_items)
            print(f"Sijainti: {pelaaja.player_location.room_name}")
        case "REPPU" | "INVENTAARIO":
            nayta_inventaario(pelaaja.player_items)
        case "LIIKU":
            print("\nKÄYTETTÄVISSÄ OLEVAT HUONEET:")
            for huone in huoneet.values():
                if huone == pelaaja.player_location:
                    print(f"- {huone.room_name} (Olet täällä)")
                else:
                    print(f"- {huone.room_name}")

            valinta = str(input("\nKirjoita huoneen nimi: ")).strip().upper()

            if valinta in huoneet:
                kohde = huoneet[valinta]
                if kohde == pelaaja.player_location:
                    print(f"Olet jo huoneessa {kohde.room_name}.")
                else:
                    pelaaja.move_to_room(kohde)
                    print(f"Siirryit huoneeseen: {pelaaja.player_location.room_name}")
            else:
                print(f"Huonetta '{valinta}' ei ole olemassa. Tarkista kirjoitusasu.")
        case "ETSI":
            current_room = pelaaja.player_location
            if not current_room.items:
                print("Huoneesta ei löytynyt mitään.")
            else:
                print(f"Löysit huoneesta {current_room.items[0].item_name}.")
                valinta = input("Haluatko ottaa esineen mukaasi? (kyllä (k) vai ei (e)): ").strip().lower()
                if valinta in ("k", "kyllä", "kylla"):
                    esine = current_room.items.pop(0)
                    pelaaja.player_items.append(esine)
                    print(f"Otit esineen {esine.item_name} mukaasi.")
                elif valinta in ("e", "ei"):
                    print("Jätit esineen huoneeseen.")
                else:
                    print("Tuntematon komento, yritä uudellen.")

        case "HELP":
            nayta_ohje()
        case _:
            print("Tuntematon komento, yritä uudelleen, voit myös kirjoittaa 'help' komentoriviin nähdäksesi kaikki komennot.")
