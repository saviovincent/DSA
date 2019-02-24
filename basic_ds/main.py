from LinkedList import LinkedList, Node
from Queue import Queue
from Stack import Stack


def main():

    ll = LinkedList()
    ll.add(Node(1))
    ll.add(Node(2))
    ll.add(Node(3))
    ll.add(Node(4))
    ll.add(Node(5))
    ll.add(Node(6))

    ll.contents()

    # queue = Queue()
    # queue.enqueue(1)
    # queue.enqueue(2)
    # queue.enqueue(3)
    # queue.enqueue(4)
    #
    # queue.dequeue()
    # queue.contents()
    # print queue.front()
    # print queue.rear()
    #
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    #
    # stack.pop()
    # stack.contents()


if __name__ == '__main__':
    main()

