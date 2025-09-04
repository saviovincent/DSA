class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
63245986        """

        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        arr = [0] * n
        arr[1] = 1
        arr[2] = 2
        count = 3
        while count <= n:
            if arr[count] == 0:
                arr[count] = self.climbStairs(n-1) + self.climbStairs(n-2)
            else:
                return arr[count]

        return arr[n]



if __name__ == '__main__':
    soln = Solution()
    print(soln.climbStairs(4))