# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # if root is None:
        #     return root
        # q = [root]
        # ans = 1
        # while q:
        #     ans = max(ans, len(q))
        #     for i in range(len(q)):
        #         el = q.pop(0)
        #         if el and el.left:
        #             q.append(el.left)
        #         else:
        #             q.append(None)
        #         if el and el.right:
        #             q.append(el.right)
        #         else:
        #             q.append(None)
        # return ans

        def dfs(root):
            if root is None:
                return 0
            lh = dfs(root.left)
            rh = dfs(root.right)
            return 1 + max(lh, rh)

        return pow(2, dfs(root) - 1)


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
    tree.right.right = TreeNode(100)

    soln = Solution()
    my_tree = soln.widthOfBinaryTree(tree)
    print(my_tree)
