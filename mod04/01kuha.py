minimiPituus = 37
while True:
    try:
        kuhaPituus = float(input("Syötä kuhan pituus senttimetreinä (cm): "))
    except ValueError:
        print("Syötä luku")
        continue

    if kuhaPituus >= minimiPituus:
        print("Kuha ei ole alamittainen.")
        break

    elif kuhaPituus < minimiPituus:
        print("Kuha on alamittainen, päästä takaisin järveen. Kuha on " + str((minimiPituus - kuhaPituus)) + " senttiä alimmasta sallitusta pyyntimitasta")
        break