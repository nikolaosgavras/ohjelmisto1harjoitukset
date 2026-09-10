class Dog:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year


dogs = [(Dog("Pekka", 2020)), (Dog("Paavo", 2015)), (Dog("Veeti", 2022))]

print(f"{dogs[0].name} was born in {dogs[0].birth_year}." )

for dog in dogs:
    print(f"{dog.name} was born in {dog.birth_year}." )

koirat = []
svuosi = 2016
nimi = "a"

for i in range(10):
    koirat.append(Dog(nimi, svuosi))
    svuosi += 1
    nimi = chr(ord(nimi) + 1)
for koira in koirat:
    print(koira.name)
    print(koira.birth_year)