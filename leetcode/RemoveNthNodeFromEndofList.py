# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        tmp1 = ListNode(-1, head)
        tmp2 = ListNode(-1, head)
        if head.next is None:
            head = head.next
            return head
        while n > 0:
            tmp1 = tmp1.next
            n -= 1

        while tmp1 and tmp1.next:
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        tmp2.next = tmp2.next.next

        return head


if __name__ == '__main__':
    soln = Solution()
    list = ListNode(1)
    list.next = ListNode(2)
    # list.next.next = ListNode(3)
    # list.next.next.next = ListNode(4)
    # list.next.next.next.next = ListNode(5)
    rslt = soln.removeNthFromEnd(list, 2)
    tmp = rslt
    while tmp is not None:
        print(str(tmp.val) + " -> ", end="")
        tmp = tmp.next
    print("END")
