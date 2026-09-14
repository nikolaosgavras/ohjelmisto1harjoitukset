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
        self.travelled_distance = self.current_speed * hours
        return
        

car1 = Car("ABC-123", 142)
print(f"Registration number: {car1.reg_num}")
print(f"Max speed: {car1.max_speed} km/h\n")

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

car1.currentSpeed()


car1.drive(1.5)
print(f"Distance travelled: {car1.travelled_distance} km")

        