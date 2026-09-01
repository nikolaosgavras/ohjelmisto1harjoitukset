import random

while True:
    userInput = int(input("Kuinka monta pistettä arvotaan?: "))
    n = 0

    for _ in range(userInput):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            n += 1

    pii_likiarvo = 4 * n / userInput
    print(f"Pii:n likiarvo: {pii_likiarvo}")
