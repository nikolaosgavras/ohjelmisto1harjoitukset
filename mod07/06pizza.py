import math

def calculatePricePerSquareMeter(pizzaRadius, pizzaPrice):
    area = math.pi * (pizzaRadius / 100) ** 2
    pricePerSquareMeter = pizzaPrice / area
    return pricePerSquareMeter

while True:
    try:
        pizza1Radius = float(input("Syötä ensimmäosen pizzan halkaisija senttimetreinä: ")) / 2
        pizza1Price = float(input("Syötä ensimmäisen pizzan hinta euroina: "))
        pizza1HintaNeliometri = calculatePricePerSquareMeter(pizza1Radius,pizza1Price)
        pizza2Radius = float(input("Syötä toisen pizzan halkaisija senttimetreinä: ")) / 2
        pizza2Price = float(input("Syötä toisen pizzan hinta: "))
        pizza2HintaNeliometri = calculatePricePerSquareMeter(pizza2Radius,pizza2Price)

        if pizza1HintaNeliometri > pizza2HintaNeliometri:
            print("Ensimmäinen pizza antaa paremman vastineen rahalle")
            break
        elif pizza2HintaNeliometri < pizza1HintaNeliometri:
            print("Toinen pizza antaa paremman vastineen rahalle")
            break
        else:
            print("Virhe, yritä uudelleen.")
            continue
    except ValueError:
        print("Syötä luku")
        continue








