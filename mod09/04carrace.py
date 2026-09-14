""" Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: “ABC-1”, “ABC-2” and so on. Now the race begins. One per every hour of the race, the following operations are performed:

The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accelerate method.
Each car is made to drive for one hour. This is done with the drive method.
The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are printed out formatted into a clear table.

 """

import random

class Car:
    def __init__(self, regnro, maxspeed):
        self.reg_num = regnro
        self.max_speed = maxspeed
        self.current_speed = 0
        self.travelled_distance = 0

    def currentSpeed(car):
        print(f"Current speed: {car.current_speed} km/h")

    def accelerate(self, speedchange):
        self.speed_change = speedchange
        if self.current_speed + speedchange > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed + speedchange < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed + speedchange
        return

    def drive(self, hours):
        self.hours_driven = hours
        # formula for distance = speed x time
        self.travelled_distance += self.current_speed * hours
        return


carsList = []
x = 0

for i in range(10):
    carsList.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))

# Race
winner = None
hours = 0

while winner == None:
    hours += 1
    for car in carsList:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        print(car.travelled_distance)
        if car.travelled_distance >= 10000:
            winner = car
            break

for car in carsList:
    print("-----------------------------")
    print(f"{car.reg_num} | {car.max_speed} km/h | {car.travelled_distance} km")


        