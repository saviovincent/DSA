"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        p1 = p
        q1 = q
        while p1 != q1:
            if p1.parent:
                p1 = p1.parent
            else:
                p1 = q

            if q1.parent:
                q1 = q1.parent
            else:
                q1 = p
        return p1


if __name__ == '__main__':
    soln = Solution()
    soln.lowestCommonAncestor()
