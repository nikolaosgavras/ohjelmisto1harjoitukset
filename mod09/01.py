class Car:
    def __init__(self, regnro, maxspeed):
        self.reg_num = regnro
        self.max_speed = maxspeed
        self.current_speed = 0
        self.travelled_distance = 0

car1 = Car("ABC-123", "142km/h")
print(car1.reg_num)
print(car1.max_speed)
        