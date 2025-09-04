import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n >= 2:
            arr = (n+1) * [True]
            arr[0] = arr[1] = False

            for i in range(2, int(math.pow(n, 0.5))+1):
                for j in range(2 * i, n+1, i):
                    arr[j] = False

            count = 0
            # print(arr)
            for i in arr:
                if i:
                    count += 1
            return count
        else:
            return 0

if __name__ == '__main__':
    soln = Solution()
    print(soln.countPrimes(0))
