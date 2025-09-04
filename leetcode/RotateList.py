# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        tmp = head
        length = 0
        while tmp.next:
            length += 1
            tmp = tmp.next

        length += 1
        tmp.next = head

        k = k % length
        tmp = head
        prev = None

        while k > 0:
            prev =tmp
            tmp = tmp.next
            k -= 1

        head = tmp.next
        tmp.next = None
        return head


if __name__ == '__main__':
    soln = Solution()
    list = ListNode(1)
    list.next = ListNode(2)
    # list.next.next = ListNode(3)
    # list.next.next.next = ListNode(4)
    # list.next.next.next.next = ListNode(5)
    rslt = soln.rotateRight(list, 1)
    tmp = rslt
    while tmp is not None:
        print(str(tmp.val) + " -> ", end="")
        tmp = tmp.next
    print("END")
