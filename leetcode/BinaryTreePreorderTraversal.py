# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        stack = [root]
        arr = []

        while stack:

            el = stack.pop()
            arr.append(el.val)
            if el.right is not None:
                stack.append(el.right)
            if el.left is not None:
                stack.append(el.left)

        return arr

    #     arr = []
    #     # self.traverseTree(root, arr)
    #     self.iterTraverse(root, arr)
    #     return arr
    #
    # def traverseTree(self, root, arr):
    #
    #     if root is None:
    #         return
    #
    #     arr.append(root.val)
    #     self.traverseTree(root.left, arr)
    #     self.traverseTree(root.right, arr)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    soln = Solution()
    print(soln.preorderTraversal(tree))
