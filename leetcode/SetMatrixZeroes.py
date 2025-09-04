class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # set 1st row and col to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # set all cols to 0
        for i in matrix[0]:
            if matrix[0][i] == 0:

    def set_col_zero(self, col, tot):



if __name__ == '__main__':
    soln = Solution()
    print(soln.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
