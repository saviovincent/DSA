class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # n = int(no)
        # count = 0
        # while n != 0:
        #     digit = n % 10
        #     if digit == 1:
        #         count += 1
        #     n = n // 10
        # return count

        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count


if __name__ == '__main__':
    soln = Solution()
    print(soln.hammingWeight(31))
