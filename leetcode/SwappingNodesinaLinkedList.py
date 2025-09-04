# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return head

        tmp1 = head
        count = k

        while count > 1:
            count -= 1
            tmp1 = tmp1.next

        node1 = tmp1

        node2 = head
        count = k
        while tmp1.next:
            count -= 1
            tmp1 = tmp1.next
            node2 = node2.next

        node1.val, node2.val = node2.val, node1.val
        return head


if __name__ == '__main__':
    soln = Solution()
    list = ListNode(1)
    list.next = ListNode(2)
    list.next.next = ListNode(3)
    list.next.next.next = ListNode(4)
    list.next.next.next.next = ListNode(5)
    rslt = soln.swapNodes(list, 3)
    tmp = rslt
    while tmp is not None:
        print(str(tmp.val) + " -> ", end="")
        tmp = tmp.next
    print("END")
