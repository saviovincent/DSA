# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        dummy = ListNode(-1, head)
        tmp = head
        count = 0
        while count < left - 1:
            tmp = tmp.next
            count += 1
        ptr1 = tmp
        ptr3 = None
        while count <= right:
            ptr3 = tmp
            tmp = tmp.next
            count += 1
        ptr2 = tmp
        ptr3.next = None

        start, end = self.reverseList(ptr1.next)
        ptr1.next = start
        end.next = ptr2
        return head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        first = None
        second = head
        third = head.next
        while third is not None:
            second.next = first
            first = second
            second = third
            third = third.next
        second.next = first
        return second, head


if __name__ == '__main__':
    soln = Solution()
    list = ListNode(1)
    list.next = ListNode(2)
    # list.next.next = ListNode(3)
    # list.next.next.next = ListNode(4)
    list = soln.reverseBetween(list, 1, 2)
    print(list)