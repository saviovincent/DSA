# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.check(root.left, root.right)

        # return self.isSymmetricIter(root)

    def check(self, t1, t2):

        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        return t1.val == t2.val and self.check(t1.left, t2.right) and self.check(t1.right, t2.left)

    # def isSymmetricIter(self, root):
    #
    #     queue = [root, root]
    #     while queue:
    #         t1 = queue.pop(0)
    #         t2 = queue.pop(0)
    #         if t1 is None and t2 is None:
    #             return True
    #         elif t1 is None or t2 is None:
    #             return False
    #         elif t1.val != t2.val:
    #             return False
    #         queue.append(t1.left)
    #         queue.append(t2.right)
    #         queue.append(t1.right)
    #         queue.append(t2.left)
    #     return True


if __name__ == '__main__':
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    soln = Solution()
    print(soln.isSymmetric(tree1, tree2))
