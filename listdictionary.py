# Create a list named 'cars'
cars = [
    # First car (dictionary)
    {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2018
    },
    # Second car (dictionary)
    {
        "make": "Ford",
        "model": "Focus",
        "year": 2020
    },
    # Third car (dictionary)
    {
        "make": "VW",
        "model": "ID.3",
        "year": 2023
    }
]

for car in cars:
    #print(car["make"],car["model"],car["year"])
    print(f"Merkki: {car["make"]} \nMalli: {car["model"]} \nVuosimalli: {car["year"]}\n")