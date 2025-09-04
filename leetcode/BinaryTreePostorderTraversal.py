# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def postorderTraversal(self, root):

        arr = []
        # self.traverseTree(root, arr)
        self.iterTraverse(root, arr)
        return arr

    def traverseTree(self, root, arr):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return

        self.traverseTree(root.left, arr)
        self.traverseTree(root.right, arr)
        arr.append(root.val)

    def iterTraverse(self, root, arr):

        if root is None:
            return

        stack = [root]
        stack2 = []

        while len(stack) > 0:

            el = stack.pop()
            stack2.append(el.val)
            if el.left is not None:
                stack.append(el.left)
            if el.right is not None:
                stack.append(el.right)

        while stack2:
            el = stack2.pop()
            arr.append(el)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    soln = Solution()
    print(soln.postorderTraversal(tree))
