def etsi(pelaaja):
    current_room = pelaaja.player_location
    if not current_room.items:
        print("Huoneesta ei löytynyt mitään.")
    else:
        print(f"Löysit huoneesta {current_room.items[0].item_name}.")
        valinta = input("Haluatko ottaa esineen mukaasi? (kyllä (k) vai ei (e)): ").strip().lower()
        if valinta in ("k", "kyllä", "kylla"):
            esine = current_room.items[0]
            pelaaja.take_item(esine)
            print(f"Otit esineen {esine.item_name} mukaasi.")
        elif valinta in ("e", "ei"):
            print("Jätit esineen huoneeseen.")
        else:
            print("Tuntematon komento, yritä uudellen.")
