class Elevator:
    def __init__(self, bottomFloor, topFloor, currentFloor = None):
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor
        self.currentFloor = currentFloor if currentFloor is not None else bottomFloor

    def go_to_floor(self, futureFloor):
        if not self.bottomFloor <= futureFloor <= self.topFloor:
            print(f"Floor {futureFloor} is out of range.")
            return
        if futureFloor > self.currentFloor:
            for _ in range(futureFloor - self.currentFloor):
                self.floor_up()
        elif futureFloor < self.currentFloor:
            for _ in range(self.currentFloor - futureFloor):
                self.floor_down()
    
    def floor_up(self):
        self.currentFloor = self.currentFloor + 1
        print(f"Moving up a floor, now at floor {self.currentFloor}")
        return

    def floor_down(self):
        self.currentFloor = self.currentFloor - 1
        print(f"Moving down a floor, now at floor {self.currentFloor}")
        return


a = Elevator(0, 10)

a.go_to_floor(11)
