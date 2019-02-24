class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.current = None

    def add(self, node):

        if self.head is None:
            self.head = node
            self.current = node

        else:
            self.current.next = node
            self.current = self.current.next

    def contents(self):

        temp = self.head

        while temp is not None:

            print temp.data
            temp = temp.next


    def addFirst(self, node):

    def addLast(self, node):

    def addMiddle(self, node):

    def removeFirst(self, node):
    def removeLast(self, node):

    def removeMiddle(self, node):

    def peekFirst(self):

    def peekLast(self):

