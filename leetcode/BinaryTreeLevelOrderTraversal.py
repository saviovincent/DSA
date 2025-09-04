# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        queue = [root]
        rslt = []

        while queue:
            nodes_in_current_level = []
            for i in range(0, len(queue)):
                el = queue.pop(0)
                nodes_in_current_level.append(el.val)
                if el.left is not None:
                    queue.append(el.left)
                if el.right is not None:
                    queue.append(el.right)

            rslt.append(nodes_in_current_level)

        return rslt


if __name__ == '__main__':
    tree = TreeNode(1)
    # tree.left = TreeNode(2)
    # tree.right = TreeNode(3)

    soln = Solution()
    print(soln.levelOrder(tree))
