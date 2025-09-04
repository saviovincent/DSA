class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False

        mid_row = len(matrix)//2
        mid_col = len(matrix[0])//2

        if target == matrix[mid_row][mid_col]:
            return True
        elif target > matrix[mid_row][mid_col]:
            return self.searchMatrix(matrix[mid_row:][mid_col:])
        elif target < matrix[mid_row][mid_col]:
            return self.searchMatrix(matrix[:mid_row][:mid_col])

if __name__ == '__main__':
    soln = Solution()
    print(soln.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))