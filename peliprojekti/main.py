# importataan kaikki tarvittavat luokat ja funktiot
from classes.player import Player
from classes.room import Room
from classes.item import Item
from pathlib import Path
from functions.lopeta_peli import lopeta_peli
from functions.nayta_ohje import nayta_ohje
from functions.nayta_inventaario import nayta_inventaario
from functions.poista_esine import poista_esine
from functions.nayta_tiedot import nayta_tiedot
from functions.liiku import liiku
from functions.etsi import etsi
from functions.korjaa import korjaa
from functions.tallenna_peli import tallenna_peli
from functions.load_save import load_save


# Luodaan huone objektit ja annetaan niille erilaisia arvoja
aula = Room("Aula", "Aseman keskus. Punaiset varovalot vilkkuvat seinillä ja lämpömittari laskee.")
tyopaja = Room("Työpaja", "Täynnä työkaluja ja varaosia vihreän energian laitteisiin.")
katto = Room("Katto", "Tuulinen kattotasanne. Aurinkopaneelit ovat lumen peitossa ja kaipaavat huoltoa.")
kallio = Room("Tuulikallio", "Korkea ja kylmä ulkokallio, jossa seisoo suuri jäinen tuulivoimala.")
kellari = Room("Kellari", "Höyryinen tila, jonne syvältä kalliosta saapuvat maalämpöputket.")

# luodaan sanakirja että voidaan helposti viitata objekteihin funktioissa
huoneet = {
    "AULA": aula,
    "TYÖPAJA": tyopaja,
    "KATTO": katto,
    "TUULIKALLIO": kallio,
    "KELLARI": kellari,
}

# luodaan tarinaan liittyvät esineet
jakoavain = Item("Jakoavain", 0.8)
aurinkokenno = Item("Aurinkokenno", 1.5)
kiipeilyvaljaat = Item("Kiipeilyvaljaat", 2.0)
voiteluoljy = Item("Voiteluöljy", 0.5)
venttiiliavain = Item("Venttiiliavain", 1.2)

# laitetaan tarinaesineitä eri huoneisiin
kallio.items.append(jakoavain)
kellari.items.append(aurinkokenno)
aula.items.append(kiipeilyvaljaat)
katto.items.append(voiteluoljy)
tyopaja.items.append(venttiiliavain)

pelaaja, age = load_save(huoneet) # kysytään onko pelaajalla tallennusta load save funktiolla, jos ei, aloitetaan uusi peli
ladattu = pelaaja is not None
if not ladattu:
    while True:
        try:
            age = int(input("Syötä ikäsi: "))
            break
        except ValueError:
            print("Syötä numero")
    name = input("Syötä nimesi: ")
    if age < 12:
        print("Käyttäjän ikä on liian alhainen. Ohjelma suljetaan.")
        raise SystemExit
    pelaaja = Player(name, [], aula)

print(f"\nTervetuloa {pelaaja.player_name}!")
nayta_tiedot(pelaaja.player_name, age, pelaaja.player_items)
print("Voit kirjoittaa 'help' nähdäksesi kaikki komennot.\n")

project_path = Path(__file__).resolve().parent
with (project_path / "intro.txt").open("r", encoding="utf-8") as file:
    print(file.read())
with (project_path / "instructions.txt").open("r", encoding="utf-8") as file:
    print(file.read())

if ladattu:
    print(f"\nJatketaan tallennuksesta. Olet huoneessa: {pelaaja.player_location.room_name}")
    nayta_inventaario(pelaaja.player_items)

while True: # komentorivi valikko pelaamiseen ja erilaisiin pelin toimintoihin
    nayta_ohje()
    userCommandInput = input("\nSyötä komento: ").upper().strip()
    match userCommandInput:
        case "LOPETA" | "QUIT":
            lopeta_peli()
        case "TIEDOT":
            nayta_tiedot(pelaaja.player_name, age, pelaaja.player_items)
            print(f"Sijainti: {pelaaja.player_location.room_name}")
        case "REPPU" | "INVENTAARIO":
            nayta_inventaario(pelaaja.player_items)
        case "LIIKU":
            liiku(huoneet, pelaaja)
        case "ETSI":
            etsi(pelaaja)
        case "KORJAA" | "AKTIVOI":
            korjaa(pelaaja)
        case "POISTA":
            poista_esine(pelaaja.player_items)
        case "TALLENNA":
            tallenna_peli(pelaaja, age, huoneet)
        case "HELP":
            nayta_ohje()
        case _:
            print("Tuntematon komento, yritä uudelleen.")
