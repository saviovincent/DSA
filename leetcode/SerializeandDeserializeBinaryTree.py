# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __init__(self):
        self.str = ""
        self.count = -1

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            self.str += "N,"
            return self.str
        self.str += str(root.val) + ","
        self.serialize(root.left)
        self.serialize(root.right)
        return self.str[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return []
        return self.helper(data.split(","))

    def helper(self, data):

        self.count += 1
        if self.count < len(data):
            if data[self.count] == "N":
                return None

            node = TreeNode(data[self.count])
            node.left = self.helper(data)
            node.right = self.helper(data)
            return node
        else:
            return None


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)

    codec = Codec()
    tmp = codec.serialize(None)
    print(tmp)
    node = codec.deserialize(tmp)
    print(node)

    # deser = Codec()
    # ans = deser.deserialize(ser.serialize(root))
