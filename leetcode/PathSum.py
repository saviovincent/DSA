# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        # if root is None:
        #     return False
        # curr_sum = 0
        #
        #
        # def dfs(root, targetSum, curr_sum):
        #     found_left = found_right = False
        #     if root.left is None and root.right is None:
        #         if curr_sum + root.val == targetSum:
        #             return True
        #         else:
        #             return False
        #     curr_sum += root.val
        #     if root.left:
        #         found_left = dfs(root.left, targetSum, curr_sum)
        #     if root.right:
        #         found_right = dfs(root.right, targetSum, curr_sum)
        #     return found_left or found_right
        #
        # return dfs(root, targetSum, curr_sum)

        if root is None:
            return False

        targetSum -= root.val
        if root.left is None and root.right is None:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.left, targetSum)


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
    print(soln.hasPathSum(None, 0))
