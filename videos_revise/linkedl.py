class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:

    def __init__(self):
        self.head = None

    def add_last(self, data):
        if not self.head:
            self.head = Node(data)
            return
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = Node(data)

    def printLL(self):
        tmp = self.head
        while tmp is not None:
            print(str(tmp.data) + " -> ", end="")
            tmp = tmp.next
        print("END")

    def rec_add(self, data, tmp):
        if not self.head:
            self.head = Node(data)
            return
        if tmp.next is None:
            tmp.next = Node(data)
            return
        self.rec_add(data, tmp.next)

    def add_at_index(self, data, index, tmp):
        """
        will only work in middle not at first/last positions
        """
        if index <= 0:
            new_node = Node(data)
            new_node.next = tmp.next
            tmp.next = new_node
            return
        self.add_at_index(data, index - 1, tmp.next)

    def middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def remove_dup(self):
        slow = self.head
        fast = self.head
        while slow.next is not None:
            while fast.next and fast.data == fast.next.data:
                fast = fast.next
            fast = fast.next
            slow.next = fast
            slow = fast

    def merge_sorted(self, head1, head2):
        pass

    def merge_sort(self):
        pass

    def reverse(self, node):
        if node is None:
            return node
        tmp = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return tmp

    # -------- Shraddha --------------

    def remove_nth_from_last(self):
        pass

    def palindrome_ll(self):
        pass

    def cycle(self):
        pass

    def cycle_length(self):
        pass

    def cycle_start_node(self):
        pass

    # ------- FCC -------------------

    def zipper_list(self, head1, head2):

        tmp1 = head1.head
        tmp2 = head2.head

        dummy_head = Node(-1)
        dummy = dummy_head
        count = 0

        while tmp1 and tmp2:
            if count % 2 == 0:
                dummy.next = tmp1
                tmp1 = tmp1.next
            else:
                dummy.next = tmp2
                tmp2 = tmp2.next

            dummy = dummy.next
            count += 1

        if tmp1:
            dummy.next = tmp1
        else:
            dummy.next = tmp2
        return dummy_head.next

    def length(self, binary):
        count = 0
        tmp = binary
        while tmp.next:
            count += 1
            tmp = tmp.next
        return count


if __name__ == '__main__':
    ll = LL()

    ll.add_last(1)
    ll.add_last(0)
    ll.add_last(0)
    ll.add_last(1)

    print(ll.length(ll))


    # ll.printLL()
    #
    # ll1 = LL()
    # ll1.add_last(100)
    # ll1.add_last(200)
    # ll1.printLL()
    #
    # ll1 = ll.zipper_list(ll, ll1)
    # print(ll1)
    # ll.add_at_index(5, 2 - 1, ll.head)
    # ll.printLL()
    # print(ll.middle())

    # ll.reverse(ll.head)
    # ll.printLL()

    # ll.add_last(1)
    # ll.add_last(1)
    # ll.add_last(2)
    # ll.add_last(3)
    # ll.add_last(3)
    # ll.add_last(3)
    # ll.add_last(4)
    # ll.printLL()
    #
    # ll.remove_dup()
    # ll.printLL()
    #
    #
    #
    # ll.rec_add(1, ll.head)
    # ll.rec_add(2, ll.head)
    # ll.rec_add(3, ll.head)
    # ll.printLL()
