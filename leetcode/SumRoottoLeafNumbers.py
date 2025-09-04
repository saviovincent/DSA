# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root, curr_sum):
            if root is None:
                return

            if root.left is None and root.right is None:
                self.ans += curr_sum * 10 + root.val
                return

            curr_sum = curr_sum * 10 + root.val
            dfs(root.left,curr_sum)
            dfs(root.right, curr_sum)

        curr_sum = 0
        self.ans = 0
        dfs(root, curr_sum)
        return self.ans


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
    print(soln.sumNumbers(tree))
