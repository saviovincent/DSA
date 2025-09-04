class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            el, cur_min = self.stack[len(self.stack) - 1]
            if cur_min > val:
                self.stack.append((val, val))
            else:
                self.stack.append((val, cur_min))

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return None
        else:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[len(self.stack) - 1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[len(self.stack) - 1][1]


if __name__ == '__main__':
    soln = MinStack()

    soln.push(2)
    print(soln.getMin())
    soln.push(0)
    print(soln.getMin())
    soln.push(1)
    print(soln.getMin())

    print(soln.pop())
    print(soln.getMin())
    print(soln.pop())
    print(soln.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
