class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            rslt=self.validate_row(i)
            if not rslt:
                return False
        for i in zip(board):
            rslt=self.validate_row(list(i))
            if not rslt:
                return False





    def validate_row(self, row):
        map = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        for i in row:
            if i == ".":
                continue
            elif map[row] < 0:
                return False
            else:
                map[row] = map[row] - 1
        return True

    def validate_col(self, row):
        map = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        for i in row:
            if i == ".":
                continue
            elif map[row] < 0:
                return False
            else:
                map[row] = map[row] - 1
        return True

    def validate_grid(self, grid):
        map = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        for j in grid:
            for i in j:
                if map[grid[j][i]] == ".":
                    continue
                elif map[grid[j][i]] < 0:
                    return False
                else:
                    map[grid[j][i]] = map[grid[j][i]] - 1
        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.isValidSudoku([["5","3",".",".","7",".",".",".","."]
                                 ,["6",".",".","1","9","5",".",".","."]
                                 ,[".","9","8",".",".",".",".","6","."]
                                 ,["8",".",".",".","6",".",".",".","3"]
                                 ,["4",".",".","8",".","3",".",".","1"]
                                 ,["7",".",".",".","2",".",".",".","6"]
                                 ,[".","6",".",".",".",".","2","8","."]
                                 ,[".",".",".","4","1","9",".",".","5"]
                                 ,[".",".",".",".","8",".",".","7","9"]]))
