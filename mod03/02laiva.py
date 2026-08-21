while True:
    luokkaInput = str(input("Syötä laivan hyttiluokka: ")).upper()
    if luokkaInput == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
        break
    elif luokkaInput == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
        break
    elif luokkaInput == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
        break
    elif luokkaInput == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")
        break
    else:
        print("Virheellinen hyttiluokka, yritä uudelleen.")

