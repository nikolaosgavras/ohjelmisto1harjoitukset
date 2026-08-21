while True:

    luku1 = input("Syötä ensimmäinen kokonaisluku: ")
    luku2 = input("Syötä toinen kokonaisluku: ")
    luku3 = input("Syötä kolmas kokonaisluku: ")

    try:
        luku1 = int(luku1)
        luku2 = int(luku2)
        luku3 = int(luku3)
        break
    except ValueError:
        print("Virhe: Syötä vain kokonaislukuja!")

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print("Summa: " + str(summa) + "\nTulo: " + str(tulo) + "\nKeskiarvo: " + str(keskiarvo))