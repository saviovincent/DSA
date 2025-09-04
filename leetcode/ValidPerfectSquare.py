class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # n = 1
        # while n <= num:
        #     if n * n < num:
        #         n = n + 1
        #     elif n * n == num:
        #         return True
        #     else:
        #         return False

        if num < 1:
            return 0
        i = 1
        j = num

        while i <= j:
            mid = (i + j) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                j = mid - 1
            else:
                i = mid + 1
        return False


if __name__ == '__main__':
    soln = Solution()
    print(soln.isPerfectSquare(9))
