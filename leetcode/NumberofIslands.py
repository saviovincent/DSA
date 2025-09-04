class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if self.count_component(grid, i, j, visited, len(grid), len(grid[0])):
                        count += 1
        return count

    def count_component(self, grid, i, j, visited, row_bound, col_bound):
        if i not in range(0, row_bound) or j not in range(0, col_bound):
            return False

        pos = str(i) + ":" + str(j)
        if pos in visited:
            return False
        if grid[i][j] == "0":
            return False

        visited.add(pos)
        self.count_component(grid, i + 1, j, visited, row_bound, col_bound)
        self.count_component(grid, i - 1, j, visited, row_bound, col_bound)
        self.count_component(grid, i, j + 1, visited, row_bound, col_bound)
        self.count_component(grid, i, j - 1, visited, row_bound, col_bound)
        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))
