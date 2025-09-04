# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        maps = {}
        minm = float('inf')
        maxm = float('-inf')

        while queue:
            el, hd = queue.pop(0)
            minm = min(minm, hd)
            maxm = max(maxm, hd)

            if hd in maps:
                maps[hd].append(el.val)
            else:
                maps[hd] = [el.val]

            if el.left:
                queue.append((el.left, hd - 1))
            if el.right:
                queue.append((el.right, hd + 1))

        rslt = []
        for i in range(minm, maxm+1):
            rslt.append(maps[i])

        return rslt


if __name__ == '__main__':
    soln = Solution()
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(soln.verticalOrder(node))
