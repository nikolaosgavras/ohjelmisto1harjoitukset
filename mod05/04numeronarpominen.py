import random

randomNumber = random.randint(1, 10)

while True:
    userInput = int(input("Arvaa luku joka on väliltä 1-10: "))
    if userInput > randomNumber:
        print("Liian suuri arvaus")
    if userInput < randomNumber:
        print("Liian pieni arvaus")
    if userInput == randomNumber:
        print("Oikein!")
        break