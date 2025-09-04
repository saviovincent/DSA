# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        return self.recurse(head)

    def recurse(self, head):
        if head is None or head.next is None:
            return head

        # 2 nodes so swap
        tmp1 = head
        head = head.next
        tmp1.next = head.next
        head.next = tmp1

        tmp = self.recurse(head.next.next)
        head.next.next = tmp
        return head

    def print(self, head):

        tmp = head
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next


if __name__ == '__main__':
    soln = Solution()
    l6 = ListNode(6)
    l5 = ListNode(5,l6)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    tmp = soln.swapPairs(l1)
    soln.print(tmp)
