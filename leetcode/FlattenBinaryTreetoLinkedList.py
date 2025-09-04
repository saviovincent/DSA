# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if root is None:
                return
            el = TreeNode(root.val)
            el.left = None
            self.tail.right = el
            self.tail = self.tail.right
            dfs(root.left)
            dfs(root.right)

        self.head = self.tail = TreeNode(-1)
        dfs(root)
        return self.head.right


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
    tree.right = TreeNode(3)
    tree.right.right = TreeNode(100)

    soln = Solution()
    my_tree = soln.flatten(tree)
    print(my_tree)
