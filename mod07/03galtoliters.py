conversion = 3.785
def muunnos(galloonat):
    laskuTulos = float(galloonat) * conversion
    galloonat = 0
    return laskuTulos

while True:
    try:
        gallons = input("Syötä galloonamäärä: ")
        if float(gallons) < 0:
            print("Negatiivinen numero, ohjelma suljetaan.")
            break
        muunnosLasku = muunnos(gallons)
        print(f"Litroina: {muunnosLasku}")
    except ValueError:
        continue


