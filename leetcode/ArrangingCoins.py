class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n

        while i <= j:

            mid = (i + j) // 2
            summ = (mid * (mid + 1)) // 2

            if summ == n:
                return mid
            elif summ > n:
                j = mid - 1
            else:
                i = mid + 1
        return j


if __name__ == '__main__':
    soln = Solution()
    print(soln.arrangeCoins(6))
