# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


count = 0


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root, root.val)
        return count

    def helper(self, root, cur_max):
        if root is None:
            return
        if root.val <= cur_max:
            global count
            count += 1
        self.helper(root.left, max(cur_max, root.val))
        self.helper(root.right, max(cur_max, root.val))


if __name__ == '__main__':
    """
            1
           / \
          2   3
         / \
        6   10
        """
    tree = TreeNode(1)
    # tree.left = TreeNode(1)
    # tree.left.left = TreeNode(3)
    # tree.right = TreeNode(4)
    # tree.right.left = TreeNode(1)
    # tree.right.right = TreeNode(5)

    soln = Solution()
    my_tree = soln.goodNodes(tree)
    print(my_tree)
