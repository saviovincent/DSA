class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        tmp = None
        while self.stack1:
            self.stack2.append(self.stack1.pop(len(self.stack1) - 1))
        if self.stack2:
            tmp = self.stack2.pop(len(self.stack2) - 1)
        while self.stack2:
            self.stack1.append(self.stack2.pop(len(self.stack2) - 1))
        return tmp

    def peek(self):
        """
        :rtype: int
        """
        tmp = None
        while self.stack1:
            self.stack2.append(self.stack1.pop(len(self.stack1) - 1))
        if self.stack2:
            tmp = self.stack2[len(self.stack2) - 1]
        while self.stack2:
            self.stack1.append(self.stack2.pop(len(self.stack2) - 1))
        return tmp

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyQueue()
    # obj.push(1)
    # obj.push(2)
    # obj.push(3)
    # obj.push(4)
    print(obj.pop())
    print(obj.pop())
    print(obj.peek())
    print(obj.empty())
