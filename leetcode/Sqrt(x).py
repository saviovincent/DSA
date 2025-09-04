import math


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 1:
            return 0
        i = 1
        j = x

        while i <= j:
            mid = (i + j) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                j = mid - 1
            else:
                i = mid + 1
        return j


if __name__ == '__main__':
    soln = Solution()
    print(soln.mySqrt(9))
