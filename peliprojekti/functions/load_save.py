import json
from pathlib import Path

from classes.item import Item
from classes.player import Player


def load_save(huoneet, save_path=None):
    valinta = input("Haluatko ladata aiemman tallennuksen? (k/e): ").strip().lower()
    if valinta not in ("k", "kylla", "kyllä"):
        return None, None
    if save_path is None:
        save_path = Path(__file__).resolve().parent.parent / "save.json"

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
            raise ValueError("Puutteellinen tallennus")
        if age < 12:
            raise ValueError("Tallennuksen pelaaja on alle 12-vuotias")
        pelaaja = Player(name, items, huoneet[location])
        # Päivitetään huoneet vasta onnistuneen latauksen jälkeen.
        for nimi, esineet in room_items.items():
            huoneet[nimi].items = esineet
        print(f"\nTallennus ladattu! Tervetuloa takaisin {name}!")
        return pelaaja, age
    except FileNotFoundError:
        print("Tallennustiedostoa 'save.json' ei löytynyt. Aloitetaan uusi peli.\n")
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
