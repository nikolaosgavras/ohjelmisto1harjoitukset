from pick import pick

while True:
    title = 'Valitse sukupuolesi:'
    options = ['Mies', 'Nainen']
    sukupuoli, index = pick(options, title)

    hemoglobiiniArvo = float(input("Syötä hemoglobiiniarvo (g/l) (älä kirjoita yksikköä): "))

    if sukupuoli == "Mies":
        if hemoglobiiniArvo < 134:
            print("Hemoglobiiniarvo on alhainen")
        elif 195 >= hemoglobiiniArvo >= 134:
            print("Hemoglobiiniarvo on normaali")
        if hemoglobiiniArvo > 195:
            print("Hemoglobiiniarvo on korkea")
    elif sukupuoli == "Nainen":
        if hemoglobiiniArvo < 117:
            print("Hemoglobiiniarvo on alhainen")
        elif 175 >= hemoglobiiniArvo >= 117:
            print("Hemoglobiiniarvo on normaali")
        if hemoglobiiniArvo > 175:
            print("Hemoglobiiniarvo on korkea")
    break

    

