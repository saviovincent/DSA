class TwoSum(object):

    def __init__(self):
        self.map = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """

        if number in self.map:
            self.map[number] += 1
        else:
            self.map[number] = 1

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        indices = []
        for k in self.map:
            if value - k in self.map:
                while self.map[k] > 0:
                    if self.map[k] == 1:
                        indices.append(self.map[k])
                    else:
                        self.map[k] -= 1

        return len(indices) == 2


if __name__ == '__main__':
    sum = TwoSum()
    sum.add(0)
    sum.add(0)
    # sum.add(0)
    # sum.add(5)
    # sum.add(1)
    # sum.add(3)
    print(sum.find(0))
    print(sum.find(7))
