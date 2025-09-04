class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.q1:
            return -1
        else:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))

        el = self.q1.pop()
        while self.q2:
            self.q1.append(self.q2.pop(0))
        return el

    def top(self):
        """
        :rtype: int
        """
        if self.q1:
            return self.q1[len(self.q1) - 1]
        return -1

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0


if __name__ == '__main__':
    soln = MyStack()
    soln.push(1)
    soln.push(2)
    soln.push(3)
    # print(soln.pop())
    # print(soln.pop())
    # print(soln.pop())

    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()
