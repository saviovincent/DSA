# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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

    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(6)
    tree1.left.right = TreeNode(10)
    tree1.right = TreeNode(3)

    soln = Solution()
    my_tree = soln.isSameTree(tree, tree1)
    print(my_tree)
