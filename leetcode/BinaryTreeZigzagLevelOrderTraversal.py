# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        ans = []
        count = 0
        while q:
            curr_el = []
            for i in range(len(q)):
                el = q.pop(0)
                curr_el.append(el.val)
                if count % 2 == 1:
                    if el.left:
                        q.append(el.left)
                    if el.right:
                        q.append(el.right)
                else:
                    if el.right:
                        q.append(el.right)
                    if el.left:
                        q.append(el.left)
            count += 1
            ans.append(curr_el)
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
    my_tree = soln.zigzagLevelOrder(tree)
    print(my_tree)
