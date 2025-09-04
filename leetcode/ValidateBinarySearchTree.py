class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root, minm, maxm):
            if root is None:
                return True
            if root.val >= maxm or root.val <= minm:
                return False
            return dfs(root.left, minm, root.val) and dfs(root.right, root.val, maxm)

        return dfs(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    # tree.left.left = TreeNode(6)
    # tree.left.right = TreeNode(10)
    tree.right = TreeNode(3)
    # tree.right.right = TreeNode(100)

    soln = Solution()
    my_tree = soln.isValidBST(tree)
    print(my_tree)
