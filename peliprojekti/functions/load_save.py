import json
from pathlib import Path

from classes.item import Item
from classes.player import Player


def load_save(huoneet, save_path=None):
    valinta = input("Haluatko ladata aiemman tallennuksen? (k/e): ").strip().lower()
    if valinta not in ("k", "kylla", "kyllä"):
        return None, None
    if save_path is None:
        save_path = Path(__file__).resolve().parent.parent / "save.txt"

    try:
        text = Path(save_path).read_text(encoding="utf-8")
        if text.lstrip().startswith("{"):
            data = json.loads(text)
            name = data["name"]
            age = data["age"]
            location = data["location"]
            if not isinstance(name, str) or type(age) is not int:
                raise ValueError("Virheellinen nimi tai ikä")
            if location not in huoneet or set(data["rooms"]) != set(huoneet):
                raise ValueError("Virheelliset huoneet")
            items = lue_esineet(data["items"])
            room_items = {
                nimi: lue_esineet(esineet)
                for nimi, esineet in data["rooms"].items()
            }
        else:
            # Vanhoissa tallennuksissa on neljä riviä ja vain esineiden nimet.
            lines = text.splitlines()
            if len(lines) < 4:
                raise ValueError("Puutteellinen tallennus")
            name, age, location = lines[0], int(lines[1]), lines[2].strip().upper()
            if location not in huoneet:
                raise ValueError("Tuntematon huone")
            room_items = {nimi: list(huone.items) for nimi, huone in huoneet.items()}
            items = []
            for nimi in filter(None, lines[3].split(",")):
                esine = None
                for esineet in room_items.values():
                    esine = next((e for e in esineet if e.item_name == nimi), None)
                    if esine is not None:
                        esineet.remove(esine)
                        break
                items.append(esine if esine is not None else Item(nimi, 1.0))

        if age < 12:
            raise ValueError("Tallennuksen pelaaja on alle 12-vuotias")
        pelaaja = Player(name, items, huoneet[location])
        # Päivitetään huoneet vasta onnistuneen latauksen jälkeen.
        for nimi, esineet in room_items.items():
            huoneet[nimi].items = esineet
        print(f"\nTallennus ladattu! Tervetuloa takaisin {name}!")
        return pelaaja, age
    except FileNotFoundError:
        print("Tallennustiedostoa 'save.txt' ei löytynyt. Aloitetaan uusi peli.\n")
    except (ValueError, KeyError, TypeError, AttributeError):
        print("Tallennustiedosto oli virheellinen tai puutteellinen. Aloitetaan uusi peli.\n")
    return None, None


def lue_esineet(data):
    if not isinstance(data, list):
        raise ValueError("Esineiden tulee olla lista")
    esineet = []
    for esine in data:
        if not isinstance(esine["item_name"], str):
            raise ValueError("Virheellinen esineen nimi")
        esineet.append(Item(esine["item_name"], esine["item_weight"]))
    return esineet
