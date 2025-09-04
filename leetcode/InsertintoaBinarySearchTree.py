# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        self.r_insertIntoBST(root, val)
        return root

    def r_insertIntoBST(self, root, val):

        if val > root.val:
            if root.right is None:
                root.right = TreeNode(val)
                return
            self.r_insertIntoBST(root.right, val)
        if root.left is None:
            root.left = TreeNode(val)
            return
        self.r_insertIntoBST(root.left, val)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)

    soln = Solution()
    soln.insertIntoBST(root, 1)
