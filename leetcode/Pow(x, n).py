class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 0
        while n > 0:
            if n % 2 != 0:
                res = res * x
            x = x * x
            n = n//2
        return res


if __name__ == '__main__':
    soln = Solution()
    print(soln.myPow(2, 2))
