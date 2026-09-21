def intro():
    print("\n--- AIRPORT DATA PROGRAM ---\n")
    print("COMMANDS:\n")

    showCommands() # call showcommands function to show commands instead of putting them here again

def showCommands():
    print("Add a new airport - 'new'")
    print("Fetch airport info - 'fetch'")
    print("Show commands/help - 'help'")
    print("Quit the program - 'exit'")

def newAirport():
    icaoCode = str(input("Enter the ICAO code of the airport: ").upper())
    airportName = str(input("Enter the name of the airport: "))

    airports[icaoCode] = airportName

def fetchAirport(icao):
    if icao in airports:
        print(airports[icao])

intro()

airports = {"EFHK":"Helsinki-Vantaa Airport"}

while True:
    userCommandInput = input("\nSyötä komento: ").upper().strip()
    match userCommandInput:
        case "NEW":
            newAirport()
        case "FETCH":
            icaoUserInput = str(input("Enter the ICAO code: ").upper())
            fetchAirport(icaoUserInput)
        case "EXIT":
            raise SystemExit
        case "HELP":
            showCommands()
        case _:
            print("Tuntematon komento, yritä uudelleen, voit myös kirjoittaa 'help' komentoriviin nähdäksesi kaikki komennot.")


        