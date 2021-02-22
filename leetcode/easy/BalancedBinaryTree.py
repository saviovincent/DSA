# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        if lh - rh > 1:
            return False
        return True

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        return 1 + max(lh, rh)


if __name__ == '__main__':
    soln = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node2.left = node1
    node1.left = node3
    print(soln.isBalanced(node2))
