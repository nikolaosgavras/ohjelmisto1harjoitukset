while True:
    try:
        seasons = ("winter", "spring", "summer", "autumn")
        userInput = int(input("Syötä kuun numero (1-12): "))
        season_index = ((userInput) % 12) // 3
        print(seasons[season_index])
        break
    except ValueError:
        print("Syötä kokonaisluku")
        continue