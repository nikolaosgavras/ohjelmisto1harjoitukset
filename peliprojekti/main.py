import random

while True:
    try:
        age = int(input("Syötä ikäsi: "))
        break
    except ValueError:
        print("Syötä numero")

name = str(input("Syötä nimesi: "))
if age < 12:
    print(f"Käyttäjän ikä on liian alhainen. Ohjelma suljetaan.")
    raise SystemExit
print(f"Tervetuloa {name}!")
while True:
    userCommandInput = input("Syötä komento: ").upper().strip()
    match userCommandInput:
        case "LOPETA":
            print("Suljetaan ohjelma.")
            raise SystemExit
        case "IKÄ":
            print(f"Olet {age} vuotta vanha.")
        case "RANDOMSANA":
            sanat = ["Viikko", "Pöytä", "Pannu", "Juomalasi", "Lompakko"]
            print(sanat[random.randint(0, 4)])
        case "HELP":
            print("Komennot: ikä, randomsana, help, lopeta")
        case _:
            print("Tuntematon komento, yritä uudelleen, voit myös kirjoittaa 'help' komentoriviin nähdäksesi kaikki komennot.")

          
