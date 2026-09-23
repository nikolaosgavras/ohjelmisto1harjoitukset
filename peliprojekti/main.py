from classes.player import Player
from classes.room import Room
from classes.item import Item
from functions.lopeta_peli import lopeta_peli
from functions.nayta_ohje import nayta_ohje
from functions.nayta_inventaario import nayta_inventaario
from functions.poista_esine import poista_esine
from functions.nayta_tiedot import nayta_tiedot


# käytän sleep funktiota tarinassa
import time


ladattu = False
ladattu_huone = None
ladatut_esineet = []

valinta = input("Haluatko ladata aiemman tallennuksen? (k/e): ").strip().lower()
if valinta in ("k", "kylla", "kyllä"):
    try:
        with open("save.txt", "r") as file:
            data = file.read().splitlines()
        if len(data) >= 4:
            name = data[0]
            age = int(data[1])
            ladattu_huone = data[2].strip().upper()
            ladatut_esineet = [e for e in data[3].strip().split(",") if e]
            ladattu = True
            print(f"\nTallennus ladattu! Tervetuloa takaisin {name}!")
        else:
            print("Tallennustiedosto oli puutteellinen. Aloitetaan uusi peli.\n")
    except FileNotFoundError:
        print("Tallennustiedostoa 'save.txt' ei löytynyt. Aloitetaan uusi peli.\n")

if not ladattu:
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
print("Voit kirjoittaa 'help' nähdäksesi kaikki komennot.\n")

with open("intro.txt", "r") as file:
    intro = file.read()
    print(intro)

with open("instructions.txt", "r") as file:
    instructions = file.read()
    print(instructions)

aula = Room("Aula", "Aseman keskus. Punaiset varovalot vilkkuvat seinillä ja lämpömittari laskee.")
tyopaja = Room("Työpaja", "Täynnä työkaluja ja varaosia vihreän energian laitteisiin.")
katto = Room("Katto", "Tuulinen kattotasanne. Aurinkopaneelit ovat lumen peitossa ja kaipaavat huoltoa.")
kallio = Room("Tuulikallio", "Korkea ja kylmä ulkokallio, jossa seisoo suuri jäinen tuulivoimala.")
kellari = Room("Kellari", "Höyryinen tila, jonne syvältä kalliosta saapuvat maalämpöputket.")

huoneet = {
    "AULA": aula,
    "TYÖPAJA": tyopaja,
    "KATTO": katto,
    "TUULIKALLIO": kallio,
    "KELLARI": kellari,
}

# tarinaan liittyvät esineet
jakoavain = Item("Jakoavain", 0.8)
aurinkokenno = Item("Aurinkokenno", 1.5)
kiipeilyvaljaat = Item("Kiipeilyvaljaat", 2.0)
voiteluoljy = Item("Voiteluöljy", 0.5)
venttiiliavain = Item("Venttiiliavain", 1.2)

kallio.items.append(jakoavain)
kellari.items.append(aurinkokenno)
aula.items.append(kiipeilyvaljaat)
katto.items.append(voiteluoljy)
tyopaja.items.append(venttiiliavain)

pelaaja = Player(name, [], aula)

if ladattu:
    if ladattu_huone in huoneet:
        pelaaja.move_to_room(huoneet[ladattu_huone])
    for esine_nimi in ladatut_esineet:
        pelaaja.player_items.append(Item(esine_nimi, 1.0))
    print(f"\nJatketaan tallennuksesta. Olet huoneessa: {pelaaja.player_location.room_name}")
    nayta_inventaario(pelaaja.player_items)

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
                    if pelaaja.player_location.description:
                        print(f"-> {pelaaja.player_location.description}")
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

        case "KORJAA" | "AKTIVOI":
            esineiden_nimet = [esine.item_name for esine in pelaaja.player_items]
            current_location = pelaaja.player_location

            if current_location == katto:
                if "Jakoavain" in esineiden_nimet and "Aurinkokenno" in esineiden_nimet:
                    print("\nKäytät jakoavainta ja asennat uuden aurinkokennon kattotasanteelle.")
                    time.sleep(1)
                    print("Aurinkopaneelit heräävät henkiin ja alkavat ladata tutkimusaseman akkuja.")
                    time.sleep(3)
                    print("Lämpötila alkaa nousta ja varovalot sammuvat.")
                    print("\nONNEKSI OLKOON! Voitit pelin palauttamalla puhtaan aurinkoenergian!")
                    lopeta_peli()
                else:
                    print("Aurinkopaneelien korjaamiseen tarvitaan 'Jakoavain' ja 'Aurinkokenno'.")
            elif current_location == kallio:
                if "Kiipeilyvaljaat" in esineiden_nimet and "Voiteluöljy" in esineiden_nimet:
                    print("\nPuet kiipeilyvaljaat, kiipeät jäiselle tuulikalliolle ja voitelet tuuliturbiinin akselin!")
                    time.sleep(1)
                    print("Suuret lavat alkavat pyöriä kovassa tunturituulessa, ja aseman sähköverkko käynnistyy!")
                    time.sleep(3)
                    print("Lämpö palaa aseman pattereihin!")
                    print("\nONNEKSI OLKOON! Voitit pelin käynnistämällä uusiutuvan tuulivoiman!")
                    lopeta_peli()
                else:
                    print("Tuulivoimalan huoltamiseen tarvitaan 'Kiipeilyvaljaat' ja 'Voiteluöljy'.")
            elif current_location == kellari:
                if "Venttiiliavain" in esineiden_nimet:
                    print("\nSaavut maalämpökeskukseen venttiiliavaimen kanssa.")
                    koodi = input("Aseta maalämpöpumpun oikea painelukema baareina (vihje: 100-200): ").strip()
                    if koodi == "150":
                        print("Käännät venttiiliä venttiiliavaimella lukemaan 150 bar!")
                        time.sleep(1)
                        print("Kuuma geoterminen höyry alkaa kiertää aseman lämmitysputkissa humisten!")
                        time.sleep(3)
                        print("Tukikohta on pelastettu jäätymiseltä!")
                        print("\nONNEKSI OLKOON! Voitit pelin hyödyntämällä geotermistä maalämpöä!")
                        lopeta_peli()
                    else:
                        print("Painelukema oli virheellinen, venttiili ei avaudu turvallisesti.")
                else:
                    print("Maalämpöpumpun säätämiseen tarvitaan 'Venttiiliavain'.")
            else:
                print("Tässä huoneessa ei ole korjattavaa energiantuotantojärjestelmää.")
                print("Voit korjata laitteistoa Katolla (aurinko), Tuulikalliolla (tuuli) tai Kellarissa (maalämpö).")
        case "POISTA":
            if not pelaaja.player_items:
                print("Reppusi on jo tyhjä, mitään ei voi poistaa.")
            elif pelaaja.player_items:
                poista_esine(pelaaja.player_items)
        case "TALLENNA":
            with open("save.txt", "w") as file:
                file.write(f"{pelaaja.player_name}\n")
                file.write(f"{age}\n")
                file.write(f"{pelaaja.player_location.room_name}\n")
                nimet = [esine.item_name for esine in pelaaja.player_items]
                file.write(",".join(nimet) + "\n")
            print("Peli tallennettu tiedostoon 'save.txt'!")
        case "HELP":
            nayta_ohje()
        case _:
            print("Tuntematon komento, yritä uudelleen, voit myös kirjoittaa 'help' komentoriviin nähdäksesi kaikki komennot.")
