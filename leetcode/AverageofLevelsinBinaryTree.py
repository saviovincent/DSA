# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        q = [root]
        ans = []
        while q:
            summ = 0
            n = len(q)
            for i in range(len(q)):
                el = q.pop(0)
                summ += el.val
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            ans.append(summ / n)
        return ans


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
    my_tree = soln.averageOfLevels(tree)
    print(my_tree)
