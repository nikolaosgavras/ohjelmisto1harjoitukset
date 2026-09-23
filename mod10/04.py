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

class Race:

    def __init__(self, name, distance, carList):
        self.race_name = name
        self.race_distance = distance
        self.car_list = carList
        self.hours = 0
        self.counter = 0

    def hour_passes(self):
        self.hours += 1
        self.counter += 1
        if self.counter == 10:
            self.print_status()
            self.counter = 0
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        if self.race_finished != True:
            print(f"Hour {self.hours} reached:")
            for car in self.car_list:
                print(f"{car.reg_num} | {car.max_speed} km/h | {car.travelled_distance} km")
        elif self.race_finished == True:
            print(f"Race finished, end results:")
            for car in self.car_list:
                print(f"{car.reg_num} | {car.max_speed} km/h | {car.travelled_distance} km")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.race_distance:
                self.race_finished = True
        return


carList = []

for i in range(10):
    carList.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))


# Race

race = Race("Grand Demolition Derby", 8000, carList)


while race.race_finished != True:
    race.hour_passes()
    race.race_finished()

if race.race_finished == True:
    race.print_status()
