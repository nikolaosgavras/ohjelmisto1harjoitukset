def poista_esine(tavarat):
    if not tavarat:
        print("Reppusi on jo tyhjä, mitään ei voi poistaa.")
        return

    print("\nRepussasi on tällä hetkellä:")
    numero = 1
    for tavara in tavarat:
        print(f"{numero}. {tavara.item_name}")
        numero += 1
    poistettava = input("Minkä esineen haluat poistaa (nimi tai numero)? ").strip()

    if poistettava.isdigit():
        numero = int(poistettava)
        if 1 <= numero <= len(tavarat):
            poistettu = tavarat.pop(numero - 1)
            print(f"Esine '{poistettu.item_name}' poistettiin repusta.")
            return
        else:
            print("Virheellinen numero.")
            return

    valittu_tavara = None
    for tavara in tavarat:
        if tavara.item_name.lower() == poistettava.lower():
            valittu_tavara = tavara
            break

    if valittu_tavara:
        tavarat.remove(valittu_tavara)
        print(f"Esine '{valittu_tavara.item_name}' poistettiin repusta.")
    else:
        print(f"Esinettä '{poistettava}' ei löytynyt repustasi.")
