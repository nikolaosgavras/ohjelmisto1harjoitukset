class Dog:
	def __init__(self, name):
		self.dog_name = name

	def bark(self):
		print(f"{self.dog_name} Woof!")


class Hotel:
	def __init__(self, dogs):
		self.dogs = dogs

	def greet_dogs(self):
		for dog in self.dogs:
			dog.bark()

dogs = [Dog("Rascal"), Dog("Bob"), Dog("Rasmus")]

hotel = Hotel(dogs)

hotel.greet_dogs() # delegation, An outer container object delegates work to its inner objects by calling their methods (e.g. `hotel.greet_dogs()` calls `dog.bark()` on each dog).