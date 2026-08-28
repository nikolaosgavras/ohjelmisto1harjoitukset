userInput = int(input("Anna luku: "))
if userInput < 2:
    print(f"{userInput} ei ole alkuluku.")
else:
    on_alkuluku = True
    for i in range(2, int(userInput ** 0.5) + 1):
        if userInput % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print(f"{userInput} on alkuluku.")
    else:
        print(f"{userInput} ei ole alkuluku.")