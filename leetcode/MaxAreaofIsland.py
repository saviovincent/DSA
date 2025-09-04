class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        maxx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cur_max = 0
                    cur_max = self.count_component(grid, i, j, visited, len(grid), len(grid[0]), cur_max)
                    maxx = max(cur_max, maxx)
        return maxx

    def count_component(self, grid, i, j, visited, row_bound, col_bound, size):
        if i not in range(0, row_bound) or j not in range(0, col_bound):
            return size
        pos = str(i) + ":" + str(j)
        if pos in visited:
            return size
        if grid[i][j] == 0:
            return size

        visited.add(pos)
        size += 1
        size = self.count_component(grid, i + 1, j, visited, row_bound, col_bound, size)
        size = self.count_component(grid, i - 1, j, visited, row_bound, col_bound, size)
        size = self.count_component(grid, i, j + 1, visited, row_bound, col_bound, size)
        size = self.count_component(grid, i, j - 1, visited, row_bound, col_bound, size)
        return size


if __name__ == '__main__':
    soln = Solution()
    print(soln.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
