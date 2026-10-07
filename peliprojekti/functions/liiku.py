def liiku(huoneet, pelaaja):
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