# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return None
        if head.next == head:
            return head

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if slow == fast:
            slow = head
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return slow
        return None


if __name__ == '__main__':
    soln = Solution()
    list = ListNode(3)
    list.next = ListNode(2)
    list.next.next = ListNode(0)
    list.next.next.next = ListNode(-4)
    list.next.next.next.next = list.next
    node = soln.detectCycle(list)
    print(node)
