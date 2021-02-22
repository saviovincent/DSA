class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop(len(self.stack) - 1)

    def contents(self):
        print(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.contents()
    stack.pop()
    stack.contents()
