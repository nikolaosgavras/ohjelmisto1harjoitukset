class Elevator:
    def __init__(self, bottomFloor, topFloor, currentFloor = None):
        self.bottom_floor = bottomFloor
        self.top_floor = topFloor
        self.current_floor = currentFloor if currentFloor is not None else bottomFloor

    def go_to_floor(self, futureFloor):
        if not self.bottom_floor <= futureFloor <= self.top_floor:
            print(f"Floor {futureFloor} is out of range.")
            return
        if futureFloor > self.current_floor:
            for _ in range(futureFloor - self.current_floor):
                self.floor_up()
        elif futureFloor < self.current_floor:
            for _ in range(self.current_floor - futureFloor):
                self.floor_down()
    
    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"Moving up a floor, now at floor {self.current_floor}")
        return

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"Moving down a floor, now at floor {self.current_floor}")
        return


class Building:
    def __init__(self, bottomFloorNumber, topFloorNumber, amountOfElevators):
        self.building_bottom_floor = bottomFloorNumber
        self.building_top_floor = topFloorNumber
        self.building_elevator_amount = amountOfElevators
        self.elevators = []

        for _ in range(amountOfElevators):
            elevatorObject = Elevator(bottomFloorNumber, topFloorNumber)
            self.elevators.append(elevatorObject)

    def run_elevator(self, elevatorNumber, targetFloor):
        self.elevators[elevatorNumber].go_to_floor(targetFloor)

    def fire_alarm(self):
        print("FIRE ALARM, MOVING ALL ELEVATORS TO THE BOTTOM FLOOR")
        for elevator in self.elevators:
            elevator.go_to_floor(self.building_bottom_floor)
        
testBuilding = Building(0, 20, 5)

testBuilding.run_elevator(0, 3)
print(testBuilding.elevators[0].current_floor) # works as intented

testBuilding.fire_alarm()