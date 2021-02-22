class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data):
        self.root = data
        self.queue = []

    def add(self, node, root):
        if node.data > root.data:
            if root.right is None:
                root.right = node
                return
            self.add(node, root.right)
        if root.left is None:
            root.left = node
            return
        self.add(node, root.left)

    def inorder(self, root):

        if root is None:
            return

        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def preorder(self, root):

        if root is None:
            return

        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):

        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def contains(self, node, root):
        if root is None:
            return
        if root.data == node.data:
            return root.data

        if node.data > root.data:
            self.contains(node, root.right)
        self.contains(node, root.left)

    def bfs(self, root):
        self.queue.append(root)

        while len(self.queue):
            node = self.queue.pop(0)
            print(node.data)
            if node.left is not None:
                self.queue.append(node.left)
            if node.right is not None:
                self.queue.append(node.right)


def main():
    tree = Tree(Node(6))

    tree.add(Node(4), tree.root)
    tree.add(Node(8), tree.root)
    tree.add(Node(1), tree.root)
    tree.add(Node(2), tree.root)
    # tree.add(Node(7), tree.root)
    # tree.add(Node(10), tree.root)

    tree.inorder(tree.root)

    print("--------------")
    tree.bfs(tree.root)
    # tree.preorder(tree.root)
    # tree.postorder(tree.root)
    # print tree.inorder(tree.contains(Node(4), tree.root))


if __name__ == '__main__':
    main()
