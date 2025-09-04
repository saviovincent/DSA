# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return
        return self.helper(root, val)

    def helper(self, root, val):
        if root is None:
            return
        if root.val == val:
            return root
        elif root.val < val:
            return self.helper(root.right, val)
        return self.helper(root.left, val)

    def iter_search(self,root, val):
        if root is None:
            return
        while root is not None:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left
        return root
