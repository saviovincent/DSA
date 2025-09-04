# ------ Alvin -------

traversal_data = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

con_comp_data = {
    '0': ['8', '1', '5'],
    '1': ['0'],
    '5': ['0', '8'],
    '8': ['0', '5'],
    '2': ['3', '4'],
    '3': ['2', '4'],
    '4': ['3', '2']
}

cycle_data = {
    0: [1, 3],
    1: [0],
    2: [3, 4],
    3: [0, 2, 4],
    4: [2, 3]

}


def dfs(src):
    print(src)
    for i in traversal_data[src]:
        dfs(i)


def dfs_iter(src):
    stack = [src]
    while stack:
        el = stack.pop()
        print(el)
        for i in traversal_data[el]:
            stack.append(i)


def bfs(src):
    que = [src]
    while que:
        el = que.pop(0)
        print(el)
        for i in traversal_data[el]:
            que.append(i)


def el_al():
    el = [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]

    graph = {}
    for i in el:
        a, b = i
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    # print(graph)
    return graph


def has_path(graph, src, des, visited):
    if src is des:
        return True
    if src in visited:
        return
    visited.add(src)
    for i in graph[src]:
        if has_path(graph, i, des, visited):
            return True
    return False


def con_comp():
    count = 0
    visited = set()
    for i in con_comp_data:
        if find_comp(i, visited):
            count += 1
    return count


def find_comp(src, visited, cur_max):
    if src in visited:
        return cur_max
    visited.add(src)
    cur_max += 1
    for i in con_comp_data[src]:
        return find_comp(i, visited, cur_max)


def max_comp():
    maxx = 0
    visited = set()
    for i in con_comp_data:
        cur_max = 0
        cur_max = find_comp(i, visited, cur_max)
        maxx = max(cur_max, maxx)
    return maxx


def bfs_shortest_path(src, dest):
    que = [(src, 0)]
    visited = set()

    while que:
        el, dd = que.pop(0)
        if el == dest:
            return dd
        if el not in visited:
            visited.add(el)
        for i in el_al()[el]:
            que.append((i, dd + 1))


# --------- Anuj -----------

def cycle_directed(src, visited, stack):
    """
    use recursion stack to track visited elements in current flow.
    Will be reset each time dfs is started for a node
    """

    if src in stack:
        return True
    elif src in visited:
        return
    visited.add(src)
    stack.add(src)
    for i in cycle_data[src]:
        if cycle_directed(i, visited, stack):
            return True
    return False


def cycle_undirected(src, parent, visited):
    """
    Visited maintained as map to track parent of that node i.e which node introduced it
    2nd check to ignore cases where child introduces parent
    """
    if src in visited:
        if visited[src] != parent and visited[parent] != src:
            return True
        else:
            return
    visited[src] = parent
    for i in cycle_data[src]:
        if cycle_undirected(i, src, dict(visited)):
            return True
    return False


def topo_dfs(src, stack):
    for i in traversal_data[src]:
        dfs(i)
    stack.append(src)


def kahn():
    pass


def find(arr, n):
    if arr[n] == n:
        return n
    return find(arr, arr[n])


def union(arr, a, b):
    x = find(arr, a)
    y = find(arr, b)
    if x == y:
        return "Cycle or same parent"
    arr[x] = y


# ------ Shraddha ------
def all_paths(src, tar, path):
    pass


def islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        q = []
        visited.add((r, c))
        q.append((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            row, col = q.pop(0)  # do pop() to convert to dfs

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited: #bounds check
                    q.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands


if __name__ == '__main__':
    print(cycle_undirected(0, -1, {}))
    # print(bfs_shortest_path('b', 'g'))
    # print(max_comp())
    # print(has_path(el_al(), 'i', 'm', set()))
    # el_al()
    # dfs('a')
    # bfs('a')
    # dfs_iter('a')
