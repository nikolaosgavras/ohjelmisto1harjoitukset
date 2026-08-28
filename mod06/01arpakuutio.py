import random

kuutioAmountInput = int(input("Syötä arpakuutioitten määrä: "))

arpakuutioList = []

for x in range(kuutioAmountInput):
    arpakuutioList.append(random.randint(1, 6))
numbersSum = sum(arpakuutioList)
print(f"Tulos:", numbersSum)