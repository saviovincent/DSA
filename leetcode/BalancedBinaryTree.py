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

        def dfs(root):
            if root is None:
                return 0
            lh = dfs(root.left)
            rh = dfs(root.right)
            self.bf = max(self.bf, abs(lh - rh))
            return 1 + max(lh, rh)

        self.bf = 0
        dfs(root)
        return self.bf <= 1


if __name__ == '__main__':
    """
            1
           / \
          2   3
         / \
        6   10
    """
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(6)
    tree.left.right = TreeNode(10)
    # tree.right = TreeNode(3)

    soln = Solution()
    my_tree = soln.isBalanced(tree)
    print(my_tree)
