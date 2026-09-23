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