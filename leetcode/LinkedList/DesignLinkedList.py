class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.current_size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.current_size or index < 0:
            return -1
        else:
            counter = 0
            tmp = self.head
            while counter < index:
                tmp = tmp.next
                counter += 1

            if tmp is not None:
                return tmp.val
            else:
                return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """

        if self.head is None:
            self.head = Node(val)
            self.current_size += 1

        else:
            node = Node(val)
            node.next = self.head
            self.head = node
            self.current_size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """

        if self.head is None:
            self.head = Node(val)
            self.current_size += 1

        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = Node(val)
            self.current_size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list,
        the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """

        if index > self.current_size:
            return None
        elif index == self.current_size:
            self.addAtTail(val)
        elif index <= 0:
            self.addAtHead(val)

        else:
            counter = 0
            cur = self.head

            while counter < index-1:
                cur = cur.next
                counter += 1

            node = Node(val)
            node.next = cur.next
            cur.next = node
            self.current_size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= self.current_size or index < 0:
            return None
        else:
            if index is 0:
                self.head = self.head.next
            else:
                counter = 0
                cur = self.head
                prev = None
                while counter < index:
                    prev = cur
                    cur = cur.next
                    counter += 1

                if prev and cur is not None:
                    prev.next = cur.next
                else:
                    prev.next = None

    def contents(self):

        temp = self.head

        while temp is not None:
            print temp.val
            temp = temp.next

# Your MyLinkedList object will be instantiated and called as such:


if __name__ == '__main__':

    obj = MyLinkedList()

    # obj.addAtHead(1)
    # obj.addAtHead(2)
    # obj.addAtHead(3)

    obj.contents()
    print obj.deleteAtIndex(2)
