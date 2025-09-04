# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            print(root.val)
            self.ans.append(root.val)
            inorder(root.right)

        self.ans = []
        inorder(root)
        minm = float('inf')
        for i in range(0, len(self.ans)):
            for j in range(i+1, len(self.ans)):
                minm = min(minm, abs(self.ans[i] - self.ans[j]))
        return minm


if __name__ == '__main__':
    """
            6
           / \
          4   7
         / \
        3   5
    """
    tree = TreeNode(6)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(5)
    tree.right = TreeNode(7)

    soln = Solution()
    my_tree = soln.getMinimumDifference(tree)
    print(my_tree)
