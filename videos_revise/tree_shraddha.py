maxm = float('-inf')
minm = float('inf')


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Count:
    def __init__(self):
        self.count = -1


# -------- FCC ------

def tree_includes(root, target):
    if root is None:
        return False
    if root.data == target:
        return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)


def tree_sum(root):
    if root is None:
        return 0
    return root.data + tree_sum(root.left) + tree_sum(root.right)


def tree_min(root):
    if root is None:
        return None
    global minm
    minm = min(minm, root.data)
    tree_min(root.left)
    tree_min(root.right)
    return minm


def max_root_leaf_sum(root, curr_sum):
    if root.left is None and root.right is None:
        global maxm
        maxm = max(maxm, root.data + curr_sum)

    if root.left:
        max_root_leaf_sum(root.left, curr_sum + root.data)
    if root.right:
        max_root_leaf_sum(root.right, curr_sum + root.data)
    return maxm


# ---------- Shraddha -------------------
def build_tree_preorder(arr, idx):
    """
    build tree from preorder sequence. Primitive int won't work as counter, need reference type(static)
    so that each recursive call gets updated index to read
    """

    idx.count += 1
    if idx.count < len(arr):
        if arr[idx.count] == -1:
            return None

        node = Node(arr[idx.count])
        node.left = build_tree_preorder(arr, idx)
        node.right = build_tree_preorder(arr, idx)
        return node
    else:
        return None


def iter_preorder(root):
    """
    push right child first
    """
    if root is None:
        return

    stack = [root]

    while stack:
        el = stack.pop()
        print(el.data, end=" ")
        if el.right:
            stack.append(el.right)
        if el.left:
            stack.append(el.left)


def iter_inorder(root):
    """
    init stack and set curr = root.
    3 conditions - if left push to stack, if stack, pop and push right, else break
    """

    if not root:
        return

    stack = []
    curr = root

    while True:

        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            print(curr.data, end=" ")
            curr = curr.right
        else:
            break


def iter_postorder(root):
    """
    right child is visited before left, reverse of preorder traversal with right preference
    Store preorder sequence in another stack
    """
    if root is None:
        return

    stack = [root]
    rslt = []

    while stack:
        el = stack.pop()
        rslt.append(el)
        if el.left:
            stack.append(el.left)
        if el.right:
            stack.append(el.right)

    while rslt:
        print(rslt.pop().data, end=" ")


def level_order(root):
    queue = [root, None]

    while queue:
        el = queue.pop(0)
        if not queue:
            break
        if not el:
            print()
            queue.append(None)
        else:
            print(el.data, end=" ")
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def topview(root):
    """
    Use horizontal distance to calculate it. Top/Btm view reverse of each other. Use map to store it
    BFS approach since 1st occurrence required
    """
    queue = [(root, 0)]
    maps = {}

    while queue:
        el, dt = queue.pop(0)
        if dt not in maps:
            maps[dt] = el
        if el.left:
            queue.append((el.left, dt - 1))
        if el.right:
            queue.append((el.right, dt + 1))

    tmp = []
    for i in maps.values():
        tmp.append(i.data)
    return tmp


def lca(root, n1, n2):
    if root is None or root.data == n1 or root.data == n2:
        return root
    la = lca(root.left, n1, n2)
    ra = lca(root.right, n1, n2)
    if not la:
        return ra
    elif not ra:
        return la
    return root


def diameter(root):
    pass


def subtree(root):
    pass


def kth_level(root):
    pass


def kth_ancestor(root):
    pass


def min_distance_2nodes(n1, n2):
    pass


def sum_tree(root):
    pass


# ----------- BST -----------

def create():
    pass


def search():
    pass


def delete():
    pass


def validate_bst(root):
    pass


def print_in_range(root):
    pass


def mirror_bst(root):
    pass


def root_to_leaf_paths(root):
    pass


def bfs_loop(root):

    q = [root]
    while q:
        for i in range(len(q)):
            el = q.pop(0)
            print(el.data, end="")
            if el.left:
                q.append(el.left)
            if el.right:
                q.append(el.right)
        print()


if __name__ == '__main__':
    counter = Count()
    node = build_tree_preorder([1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, - 1, -1], counter)

    # ---- Shradda -----

    # level_order(node)
    # iter_preorder(node)
    # iter_inorder(node)
    # iter_postorder(node)
    # level_order(node)
    # print(height(node))
    # print(bfs_loop(node))

    # --- FCC ---

    # print(tree_includes(node,34))
    # print(tree_sum(node))
    # print(tree_min(node))
    # print(max_root_leaf_sum(node,0))

    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # root.right.left = Node(6)
    # root.right.right = Node(7)
    #
    # print(lca(root, 3, 5).data)
    # print(horizontal_distance(root)) # topview - [1, 2, 3, 4, 7]   botm view - [6, 2, 3, 4, 7]
