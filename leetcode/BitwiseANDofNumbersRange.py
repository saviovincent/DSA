class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        """
        keep right shifting unless both nos become equal. 
        Need to left shift no of times it was right shifted to find actual number
        """
        count = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            count += 1
        return left << count


if __name__ == '__main__':
    soln = Solution()
    print(soln.rangeBitwiseAnd(5, 7))
