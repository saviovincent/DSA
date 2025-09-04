# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None:
                return 0
            lh = helper(root.left)
            rh = helper(root.right)
            self.diam = max(self.diam, lh + rh + 1)
            return 1 + max(lh, rh)

        self.diam = 0
        helper(root)
        return self.diam - 1


if __name__ == '__main__':
    """
             1
            / \
           2   3
          / \
         6   9
         """
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(6)
    tree.left.right = TreeNode(9)
    tree.right = TreeNode(3)

    soln = Solution()
    print(soln.diameterOfBinaryTree(tree))
