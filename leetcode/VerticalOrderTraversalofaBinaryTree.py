# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0,0)]
        maps = {}
        minm = float('inf')
        maxm = float('-inf')

        while queue:
            el, r,c = queue.pop(0)
            minm = min(minm, c)
            maxm = max(maxm, c)

            if c in maps:
                maps[c].append((r,el.val))
            else:
                maps[c] = [(r,el.val)]

            if el.left:
                queue.append((el.left, r+1, c - 1))
            if el.right:
                queue.append((el.right, r+1, c + 1))

        rslt = []
        maps = dict(sorted(maps.items(), key=lambda x: (x[0], x[1])))

        for i in range(minm, maxm+1):
            tmp = []
            for j in range(len(maps[i])):
                tmp.append(maps[i][j][1])
            rslt.append(tmp)

        return rslt


if __name__ == '__main__':
    soln = Solution()
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(7)
    print(soln.verticalTraversal(node))
