nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta/poista joku alkio painamalla Enter: ")
while nimi != "":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta/poista alkio painamalla Enter: ")
userSelection = input("Kirjoita 'poista' jos haluat poistaa alkion tai paina enter jos haluat lopettaa: ")
while userSelection == "poista":
    nimenPoisto = input("Kirjoita alkion nimi: ")
    if nimenPoisto == "exit":
        print(nimet)
        break
    nimet.remove(nimenPoisto)
    print(nimet)
else:
    print(nimet)