# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxm = float('-inf')
        q = [root]
        while q:
            for i in range(len(q)):
                el = q.pop(0)
                maxm = max(maxm, self.sum(el))
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
        return maxm

    def sum(self, root):
        if root is None:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)


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
    print(soln.maxPathSum(tree))
