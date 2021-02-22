from basic_ds.Tree import Node
from basic_ds.Tree import Tree


def min_tree(arr):
    if not arr:
        return None

    mid = len(arr) / 2
    node = Node(arr[mid])
    node.left = min_tree(arr[:mid])
    node.right = min_tree(arr[mid + 1:])
    return node


if __name__ == '__main__':
    root = min_tree([2, 4, 6, 8, 10])
    tree = Tree(root)
    tree.inorder(root)
