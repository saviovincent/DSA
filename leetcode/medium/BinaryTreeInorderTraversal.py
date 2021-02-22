# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def __init__(self):
        self.arr = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.arr.append(root.val)
        self.inorderTraversal(root.right)
        return self.arr


