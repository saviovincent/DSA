# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # if root is None:
        #     return 0
        # lh = self.maxDepth(root.left)
        # rh = self.maxDepth(root.right)
        # return 1 + max(lh, rh)

        if root is None:
            return 0

        return self.helper(root, 0)

    def helper(self, root, depth):
        if root is None:
            return depth

        depth += 1  # should follow preorder

        lh = self.helper(root.left, depth)
        rh = self.helper(root.right, depth)
        return max(lh, rh)


if __name__ == '__main__':
    soln = Solution()

    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node1.left.left = TreeNode(3)
    print(soln.maxDepth(node1))
