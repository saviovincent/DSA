# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    found = False

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        global found
        if root is None:
            return None
        if root.val == p:
            found = True
        if root.left:
            return self.inorderSuccessor(root.left, p)
        if found:
            return root.val
        if root.right:
            return self.inorderSuccessor(root.right, p)
        return None


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    soln = Solution()
    print(soln.inorderSuccessor(root, 1))
