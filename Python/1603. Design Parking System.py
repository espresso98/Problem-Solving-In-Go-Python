class ParkingSystem:
    # Solution 1
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if (carType == 1 and self.big == 0) or (carType == 2 and self.medium == 0) or (carType == 3 and self.small == 0):
            return False
        if carType == 1: self.big -= 1
        elif carType == 2: self.medium -= 1
        elif carType == 3: self.small -= 1
        return True


# [[1,1,0],[1],[2],[3],[1]]
class ParkingSystem2:
    def __init__(self, big: int, medium: int, small: int):
        self.size = { 1: big, 2: medium, 3: small }
        # print(self.parking[1], self.parking[2], self.parking[3]) # [1,1,0]

    def addCar(self, carType: int) -> bool:
        if self.size[carType]:
            self.size[carType] -= 1
            return True
        return False


class ParkingSystem3:
    def __init__(self, big, medium, small):
        self.size = [big, medium, small]

    def addCar(self, carType):
        self.size[carType-1] -= 1
        return self.size[carType-1] >= 0

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)