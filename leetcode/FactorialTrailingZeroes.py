class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        rslt = 0
        i = 5
        while i < n:
            rslt += n//i
            i *=5
        return rslt

if __name__ == '__main__':
    soln = Solution()
    print(soln.trailingZeroes(3))