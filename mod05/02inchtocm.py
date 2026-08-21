conversion = 2.54

while True:
    try:
        userInput = float(input('Syötä tuuma-arvo: '))
        if userInput < 0:
            print("Älä syötä negatiivisia numeroita.")
            continue
        print(userInput * conversion, "cm")
        break

    except ValueError:
        print("Syötä numerinen arvo")

