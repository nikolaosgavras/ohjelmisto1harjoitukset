""" 
Extend the previously written Car class by adding two subclasses: ElectricCar and GasolineCar. 
Electric cars have the capacity of the battery in kilowatt-hours as their property. 
Gasoline cars have the volume of the tank in liters as their property.
Write initializers for the subclasses.
For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter.
 It calls the initializer of the base class to set the first two properties and then sets its capacity.
   Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l).
Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters. 
"""

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

class ElectricCar(Car):
    def __init__(self, regnro, maxspeed, batteryKWH):
        self.battery_kilowatt_hours = batteryKWH
        super().__init__(regnro, maxspeed)

class GasolineCar(Car):
    def __init__(self, regnro, maxspeed, tankLiters):
        self.tank_liters = tankLiters
        super().__init__(regnro, maxspeed)

electricCar = ElectricCar("ABC-15", 180, 52.5)
gasolineCar = GasolineCar("ACD-123", 165, 32.3)

electricCar.accelerate(140)
gasolineCar.accelerate(120)

electricCar.drive(3)
gasolineCar.drive(3)

print(f"{electricCar.reg_num} | {electricCar.travelled_distance} km")
print(f"{gasolineCar.reg_num} | {gasolineCar.travelled_distance} km")