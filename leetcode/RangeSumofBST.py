# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        self.calc(root, low, high, self.sum)
        return self.sum

    def calc(self, root, low, high, sum):
        if root is None:
            return 0
        if low <= root.val <= high:
            self.sum += root.val
        if low < root.val:
            self.calc(root.left, low, high, sum)
        if high > root.val:
            self.calc(root.right, low, high, sum)


if __name__ == '__main__':
    soln = Solution()
    node = TreeNode(9)
    node.left = TreeNode(5)
    node.right = TreeNode(11)
    node.right.left = TreeNode(10)
    node.right.right = TreeNode(13)
    print(soln.rangeSumBST(node, 5, 10))
