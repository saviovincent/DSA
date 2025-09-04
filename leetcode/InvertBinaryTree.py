# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return

        tmp1 = root.left
        tmp2 = root.right
        root.left = tmp2
        root.right = tmp1

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


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

    soln = Solution()
    my_tree = soln.invertTree(tree)
    print(my_tree)
