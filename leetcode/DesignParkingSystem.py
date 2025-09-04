class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.space = {
            1:big,
            2:medium,
            3:small
        }

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.space[carType]:
            self.space[carType] -=1
            return True
        return False

if __name__ == '__main__':
    soln = ParkingSystem(2,2,2)
    print()