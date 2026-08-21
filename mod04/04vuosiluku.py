while True:
    try:
        vuosiLuku = int(input("Syötä vuosiluku: "))
    except ValueError:
        print("Syötä vuosiluku")
        continue

    if (vuosiLuku % 4 == 0 and vuosiLuku % 100 != 0) or (vuosiLuku % 400 == 0):
        print("Vuosi on karkausvuosi.")
    else:
        print("Vuosi ei ole karkausvuosi.")
    break