class Stack:

    def __init__(self):
        self.stack = list()

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop(len(self.stack) - 1)

    def contents(self):
        print self.stack
