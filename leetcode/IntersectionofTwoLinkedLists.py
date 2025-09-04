# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB:
            return None

        len1 = 0
        len2 = 0

        tmp1 = headA
        while tmp1 is not None:
            len1 += 1
            tmp1 = tmp1.next

        tmp2 = headB
        while tmp2 is not None:
            len2 += 1
            tmp2 = tmp2.next

        diff = len1 - len2
        tmp1 = headA
        tmp2 = headB

        if diff > 0:
            while diff:
                tmp1 = tmp1.next
                diff -= 1
        else:
            diff *= -1
            while diff:
                tmp2 = tmp2.next
                diff -= 1

        while tmp1 and tmp2 and tmp1 != tmp2:
            tmp1 = tmp1.next
            tmp2 = tmp2.next

        return tmp1


if __name__ == '__main__':
    soln = Solution()
