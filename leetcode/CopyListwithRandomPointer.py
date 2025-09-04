"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        tmp = head
        sentinel = Node(-1)
        curr = sentinel
        my_map = {}

        while tmp:
            if tmp in my_map:
                curr.next = my_map[tmp]
                if tmp.random:
                    if tmp.random in my_map:
                        curr.random = my_map[tmp]
                    else:
                        new_node = Node(tmp.random.val, tmp.random.next, tmp.random)
                        my_map[new_node] = new_node

            else:
                new_node = Node(tmp.val, None, None)
                my_map[tmp] = new_node
                curr.next = new_node
                curr = new_node

                if tmp.random:
                    if tmp.random in my_map:
                        new_node.random = my_map[tmp]
                    else:
                        new_node1 = Node(tmp.random.val, tmp.random.next, tmp.random)
                        my_map[tmp] = new_node1

            tmp = tmp.next


if __name__ == '__main__':
    soln = Solution()
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)

    n1.next = n2
    n1.random = None
    n2.next = n3
    n2.random = n1
    n3.next = n4
    n3.random = n5
    n4.next = n5
    n4.random = n3
    n5.next = None
    n5.random = n1
    rslt = soln.copyRandomList(n1)

    tmp = rslt
    while tmp is not None:
        print(str(tmp.val) + " -> ", end="")
        tmp = tmp.next
    print("END")
