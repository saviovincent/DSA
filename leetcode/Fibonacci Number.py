class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        a = 1
        b = 2

        count = 0
        tmp = 0
        while count < n-1:
            tmp = a + b
            a = b
            b = tmp
            count = count +1
        return tmp

if __name__ == '__main__':
    soln = Solution()
    print(soln.fib(38))
