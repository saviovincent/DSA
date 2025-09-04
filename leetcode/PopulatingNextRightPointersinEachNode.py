"""
# Definition for a Node.

"""


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return root

        queue = [root]

        while queue:
            j = 1
            count = len(queue)
            for i in range(count):
                el = queue.pop(0)
                if j < count:
                    el.next = queue[0]
                    j += 1
                else:
                    el.next = None
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)

        return root


if __name__ == '__main__':
    soln = Solution()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # root.right.left = Node(6)
    # root.right.right = Node(7)

    node = soln.connect(root)
    print(node)
