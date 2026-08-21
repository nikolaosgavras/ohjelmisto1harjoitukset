import random

print("Kolminumeroinen koodi: ", end="")
for x in range(3):
    print(random.randint(0, 9), end="")

print("\nNelinumeroinen koodi: ", end="")
for x in range(4):
    print(random.randint(1, 6), end="")

