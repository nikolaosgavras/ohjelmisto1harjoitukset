class Dog:

    color = ""

    def __init__(self, name, birth_year, colorInput, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.color = colorInput

dog1 = Dog("Rascal", 2018, "musta")
print(Dog.color)
dog2 = Dog("Boi", 2022, "ruskea")
print(Dog.color)