# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        if not head.next:
            head = head.next
            return head

        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = prev.next.next
        slow = None

        return head

if __name__ == '__main__':
    soln = Solution()
    list = ListNode(1)
    # list.next = ListNode(2)
    # list.next.next = ListNode(3)
    # list.next.next.next = ListNode(4)
    rslt = soln.deleteMiddle(list)
    tmp = rslt
    while tmp is not None:
        print(str(tmp.val) + " -> ", end="")
        tmp = tmp.next
    print("END")