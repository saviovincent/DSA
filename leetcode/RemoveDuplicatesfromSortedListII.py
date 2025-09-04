# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        sentinel = ListNode(-101, head)
        ptr = sentinel

        prev = sentinel
        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next

        return ptr.next


if __name__ == '__main__':
    soln = Solution()
    list = ListNode(1)
    list.next = ListNode(1)
    # list.next.next = ListNode(2)
    # list.next.next.next = ListNode(2)
    # list.next.next.next.next = ListNode(5)
    rslt = soln.deleteDuplicates(list)
    curr = rslt
    while curr is not None:
        print(str(curr.val) + " -> ", end="")
        curr = curr.next
    print("END")
