# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        def dfs(root, targetSum, path, ans):
            if root is None:
                return

            path.append(root.val)
            if root.left is None and root.right is None:
                if targetSum == root.val:
                    ans.append(path)
                    return
            dfs(root.left, targetSum - root.val, list(path), ans)
            dfs(root.right, targetSum - root.val, list(path), ans)

        ans = []
        dfs(root, targetSum, [], ans)
        return ans


if __name__ == '__main__':
    """
             1
            / \
           2        3
          / \      /
         6   10   5
         """
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right = TreeNode(8)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right.left = TreeNode(5)
    tree.right.right.right = TreeNode(1)

    soln = Solution()
    print(soln.pathSum(tree, 22))
