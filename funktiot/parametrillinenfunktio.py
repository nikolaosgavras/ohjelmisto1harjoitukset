def tervehdi(kerrat):
    for i in range(kerrat):
        print("Hyvää päivää " + str(i+1) + ". kerran")
    return

print("Päivä alkaa tervehdyksillä.")
tervehdi(5)
print("Tervehditään lisää.")
tervehdi(2)

# Sama asia mutta kysytään käyttäjältä monta tervehdystä haluaa.

while True:

    try:
        userInput = int(input("Monta tervehdystä haluat?: "))
        tervehdi(userInput)
        break

    except ValueError:
        print("Syötä luku")
