class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = self.el_al(prerequisites)
        order = self.dfs(graph, [], 1)
        print(order)

    def dfs(self, graph, stack, src):
        for i in graph[src]:
            self.dfs(graph, stack, i)
        stack.append(src)
        return stack

    def el_al(self, el):
        graph = {}
        for i in el:
            a, b = i
            if b not in graph:
                graph[b] = []
            if a not in graph:
                graph[a] = []


            graph[a].append(b)
            # graph[b].append(a)

        # print(graph)
        return graph


if __name__ == '__main__':
    soln = Solution()
    print(soln.canFinish(2, [[1, 0]]))
