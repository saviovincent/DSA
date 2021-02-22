# LinkedList Implementation
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.current = None

    def addLast(self, node):

        if self.head is None:
            self.head = node
            self.current = node

        # else:
        #     self.current.next = node
        #     self.current = self.current.next

        # through single pointer

        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node
        # if node.data == 3:
        #     node.next = self.head

    def contents(self):

        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next

    def addFirst(self, node):

        if self.head is None:
            self.head = node
            self.current = node

        else:
            node.next = self.head
            self.head = node

    def removeFirst(self):

        if self.head is None:
            print("Nothing to remove")
        else:
            self.head = self.head.next

    def removeLast(self):

        if self.head is None:
            print("Nothing to remove")
        elif self.head.next is None:
            self.head = None
        else:
            prev = None
            current = self.head
            while current.next is not None:
                prev = current
                current = current.next
            prev.next = None

    def peekFirst(self):
        return self.head.data

    def peekLast(self):
        # return self.current.data

        # if only 1 pointer
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        return tmp.data

if __name__ == '__main__':
    ll = LinkedList()

    ll.addLast(Node(1))
    ll.addLast(Node(2))
    ll.addLast(Node(3))
    ll.contents()
    ll.removeLast()
    ll.contents()
