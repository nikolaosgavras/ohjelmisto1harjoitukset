names = set()

while True:
    try:
        userInput = str(input("Syötä nimi: "))
        if userInput == "":
            break
        if userInput in names:
            print("Existing name")
        if userInput not in names:
            print("New name")
        names.add(userInput)
    except ValueError:
        print("Virhe, syötä nimi")
print("Kaikki nimet:")
for name in names:
    print(name)
    