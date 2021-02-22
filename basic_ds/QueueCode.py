class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[len(self.queue)-1]

    def contents(self):
        print(self.queue)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    queue.dequeue()
    queue.contents()
    print(queue.front())
    print(queue.rear())