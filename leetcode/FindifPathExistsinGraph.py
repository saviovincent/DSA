class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if not edges:
            return False
        if edges and not edges[0]:
            return False

        al = self.el_al(edges)
        self.visited = set()

        return self.dfs(al, source, source, destination)

    def dfs(self, graph, node, src, dest):
        if dest in graph[node]:
            return True
        if node in self.visited:
            return False

        self.visited.add(node)

        for el in graph[node]:
            if el not in self.visited:
                return self.dfs(graph, el, src, dest)

        print(self.visited)
        return False

    def el_al(self, el):
        my_map = {}
        for i in range(0, len(el)):
            v1, v2 = el[i][0], el[i][1]
            if v1 in my_map:
                my_map[v1].append(v2)
            else:
                my_map[v1] = [v2]

            if v2 in my_map:
                my_map[v2].append(v1)
            else:
                my_map[v2] = [v1]

        return my_map


if __name__ == '__main__':
    soln = Solution()
    print(soln.validPath(10, [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]], 5, 9))
