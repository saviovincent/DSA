# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        mid = self.middle(head)
        reversed = self.reverseList(mid.next)
        mid.next = None
        mid = head

        sentinel = ListNode(-1)
        ptr = sentinel
        count = 0

        while mid and reversed:
            if count % 2 == 0:
                sentinel.next = mid
                mid = mid.next
            else:
                sentinel.next = reversed
                reversed = reversed.next
            sentinel = sentinel.next
            count += 1

        if mid:
            sentinel.next = mid
        if reversed:
            sentinel.next = reversed

        return ptr.next

    def middle(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):

        if head is None or head.next is None:
            return head

        prev = None
        curr = head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


if __name__ == '__main__':
    soln = Solution()
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)
    rslt = soln.reorderList(list)
    tmp = rslt
    while tmp is not None:
        print(str(tmp.val) + " -> ", end="")
        tmp = tmp.next
    print("END")
