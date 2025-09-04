# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while slow is not None and slow.next is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
