class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if self.perimeter(grid, i, j, visited, len(grid), len(grid[0])):
                        count += 1
        return count

    def perimeter(self, grid, i, j, visited, row_bound, col_bound,size):
        if i not in range(0, row_bound) or j not in range(0, col_bound):
            return 0

        pos = str(i) + ":" + str(j)
        if pos in visited:
            return size
        if grid[i][j] == "0":
            return 0

        visited.add(pos)
        self.perimeter(grid, i + 1, j, visited, row_bound, col_bound,size)
        self.perimeter(grid, i - 1, j, visited, row_bound, col_bound,size)
        self.perimeter(grid, i, j + 1, visited, row_bound, col_bound,size)
        self.perimeter(grid, i, j - 1, visited, row_bound, col_bound,size)
        return s
if __name__ == '__main__':
    soln = Solution()
    print(soln.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
