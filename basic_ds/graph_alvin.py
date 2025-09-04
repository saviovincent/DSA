from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = [
            [1, 2],
            [1, 3],
            [2, 4], [2, 3],
            [5, 2], [4, 3]
        ]

    def build_adj_list_directed(self):
        adj_list = defaultdict(list)
        for i in self.graph:
            src, dest = i[0], i[1]
            if src in adj_list:
                adj_list[src].append(dest)
            else:
                adj_list[src] = [dest]
        return adj_list

    def build_adj_list_undirected(self):
        adj_list = defaultdict(list)
        for i in self.graph:
            src, dest = i[0], i[1]
            if src in adj_list:
                adj_list[src].append(dest)
            else:
                adj_list[src] = [dest]
            if dest in adj_list:
                adj_list[dest].append(src)
            else:
                adj_list[dest] = [src]
        return adj_list

    def bfs(self, graph, node):
        if not graph or not node:
            return
        visited = set()
        queue = [node]
        visited.add(node)
        while queue:
            el = queue.pop(0)
            print(el)
            for node in graph[el]:
                if node not in visited:
                    queue.append(node)

    def dfs(self, graph, node, visited):
        visited.add(node)
        print(node)
        for el in graph[node]:
            if el not in visited:
                self.dfs(graph, el)

    def has_path(self, graph, src, dst, visited):
        if src == dst:
            return True
        if src in visited:
            return

        visited.add(src)

        for i in graph[src]:
            return self.has_path(graph, i, dst, visited)

        return False

    def has_cycle(self, graph, src, visited):
        if src in visited:
            return True

        visited.add(src)

        for i in graph[src]:
            return self.has_cycle(graph, i, visited)

        return False


if __name__ == '__main__':
    graph = Graph()
    directed_graph = graph.build_adj_list_directed()
    undirected_graph = graph.build_adj_list_undirected()
    # graph.bfs(undirected_graph, 1)
    # graph.dfs(undirected_graph, 1, set())

    print(graph.has_cycle(undirected_graph, 1, set()))
