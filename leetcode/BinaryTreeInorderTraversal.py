# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        if root is None:
            return

        stack = []
        arr = []
        current = root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            else:
                if stack:
                    el = stack.pop()
                    arr.append(el.val)
                    current = el.right
                else:
                    break
        return arr

    # def traverseTree(self, root, arr):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #
    #     if root is None:
    #         return
    #
    #     self.traverseTree(root.left, arr)
    #     arr.append(root.val)
    #     self.traverseTree(root.right, arr)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    soln = Solution()
    print(soln.inorderTraversal(tree))
