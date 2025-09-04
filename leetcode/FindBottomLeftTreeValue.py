# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return root
        q = [root]
        ans = root.val
        flag = True
        while q:
            for i in range(len(q)):
                el = q.pop(0)
                if el.left:
                    if flag:
                        ans = el.left.val
                        flag = False
                    q.append(el.left)
                if el.right:
                    if flag:
                        ans = el.right.val
                        flag = False
                    q.append(el.right)
            flag = True
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
    tree.left.right.left = TreeNode(100)

    # tree.right = TreeNode(3)

    soln = Solution()
    my_tree = soln.findBottomLeftValue(tree)
    print(my_tree)
