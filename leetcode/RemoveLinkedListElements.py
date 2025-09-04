# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return head

        sentinel = ListNode(-1, head)
        prev = sentinel
        curr = head

        while curr.next:
            if curr.val == val:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        if curr.val == val:
            prev.next = None
        else:
            prev.next = curr
        return sentinel.next


if __name__ == '__main__':
    soln = Solution()
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(1)
    # list.next.next.next = ListNode(4)
    # list.next.next.next.next = ListNode(5)
    rslt = soln.removeElements(list, 3)
    curr = rslt
    while curr is not None:
        print(str(curr.val) + " -> ", end="")
        curr = curr.next
    print("END")
