# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # merge into l1
        if l1.val > l2.val:
            self.mergeTwoLists(l2, l1)

        l1_cur = l1
        l1_prev = None
        l2_cur = l2
        l2_prev = None

        while l1_cur.next is not None and l2_cur.next is not None:

            if l1_cur.next.val <= l2_cur.val:
                l1_prev = l1_cur
                l1_cur = l1_cur.next
            else:
                l2_prev = l2_cur
                l2_cur = l2_cur.next

                l2_prev.next = l1_cur.next
                l1_cur.next = l2_prev

                l2_prev = None

                l1_prev = l1_cur
                l1_cur = l1_cur.next

        if l1_cur.next is None and l2_cur is not None:
            l1_cur.next = l2_cur

        return l1


if __name__ == '__main__':
    node_1 = ListNode(4)
    node_2 = ListNode(2, node_1)

    node_3 = ListNode(3)
    node_4 = ListNode(1, node_3)

    soln = Solution()
    merged = soln.mergeTwoLists(node_4, node_2)

    tmp = merged
    while tmp is not None:
        print tmp.val
        tmp = tmp.next

