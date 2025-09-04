class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = self.el_al(edges, n)
        count = 0
        visited = set()
        for i in graph:
            if self.count_component(i, graph, visited):
                count += 1
        return count

    def count_component(self, src, graph, visited):
        if src in visited:
            return False
        visited.add(src)
        for i in graph[src]:
            self.count_component(i, graph, visited)
        return True

    def el_al(self, edges, n):
        graph = {}
        for i in edges:
            a, b = i
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append(b)
            graph[b].append(a)

        for i in range(n):
            if i not in graph:
                graph[i] = []
        return graph


if __name__ == '__main__':
    soln = Solution()
    print(soln.countComponents(5, [[2, 3], [1, 2], [1, 3]]))
