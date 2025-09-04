# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """

        if not list1:
            return list2
        if not list2:
            return list1

        sentinel = ListNode(-1)
        ptr = sentinel

        while list1 and list2:
            if list1.val < list2.val:
                sentinel.next = list1
                list1 = list1.next
            else:
                sentinel.next = list2
                list2 = list2.next
            sentinel = sentinel.next

        if list1:
            sentinel.next = list1
        if list2:
            sentinel.next = list2

        return ptr.next


if __name__ == '__main__':
    node_2 = ListNode(3)
    node_1 = ListNode(1, node_2)

    node_4 = ListNode(4)
    node_3 = ListNode(2, node_4)

    soln = Solution()
    merged = soln.mergeTwoLists(node_1, node_3)
    print(merged)
