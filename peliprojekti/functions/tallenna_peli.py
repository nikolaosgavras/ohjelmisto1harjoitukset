from pathlib import Path
import json

def tallenna_peli(pelaaja, age, huoneet, save_path=None):
    if save_path is None:
        save_path = Path(__file__).resolve().parent.parent / "save.json"
    data = {
        "name": pelaaja.player_name,
        "age": age,
        "location": pelaaja.player_location.room_name.upper(),
        "items": [vars(esine) for esine in pelaaja.player_items],
        "rooms": {
            nimi: [vars(esine) for esine in huone.items]
            for nimi, huone in huoneet.items()
        },
    }
    with Path(save_path).open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print("Peli tallennettu tiedostoon 'save.json'!")
