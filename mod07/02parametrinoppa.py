import random

def nopanheitto(amount):
    noppaValue = random.randint(1,amount)
    return noppaValue

tahkot = int(input("Syötä nopan tahkojen yhteismäärä: "))
while True:
    noppa = nopanheitto(tahkot)
    if noppa == tahkot:
        print(noppa)
        break
    else:
        print(noppa)
    