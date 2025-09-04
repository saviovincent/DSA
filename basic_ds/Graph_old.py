from collections import defaultdict


class Graph:

    def __init__(self):
        self.visited = []
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def init_dfs(self):
        self.visited = [False] * (len(self.graph) + 1)

    def graph_dfs(self, node):

        print(node)
        self.visited[node] = True

        for i in self.graph[node]:
            if not self.visited[i]:
                self.graph_dfs(i)

    def graph_bfs(self, node):
        visited = [False] * len(self.graph)
        queue = [node]
        visited[node] = True

        while queue:
            current_node = queue.pop(0)
            print(current_node)
            for i in self.graph[current_node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def matrix_dfs(self, arr, visited, start):

        visited[start] = True
        for node in range(len(arr[start])):
            if visited[node] is False and arr[start][node] != 0:
                print("Path from {} to {} ".format(start, node))
                self.matrix_dfs(arr, visited, node)


if __name__ == '__main__':
    graph = Graph()
    # graph.add_edge(0, 1)
    # graph.add_edge(0, 2)
    # graph.add_edge(0, 3)
    # graph.add_edge(3, 2)
    # graph.add_edge(1, 2)
    #
    # print("DFS")
    # graph.init_dfs()
    # graph.graph_dfs(0)
    # print("BFS")
    # graph.graph_bfs(0)

    arr = [[0 for j in range(0, 5)] for i in range(0, 5)]
    arr[0][1] = 1
    arr[0][2] = 1
    arr[0][3] = 1
    arr[0][4] = 1
    arr[1][0] = 1
    arr[2][0] = 1
    arr[3][0] = 1
    arr[4][0] = 1
    print(arr)

    visit = [False] * 5
    print(visit)

    for i in range(0, len(arr)):
        graph.matrix_dfs(arr,[False] * 5, i)
