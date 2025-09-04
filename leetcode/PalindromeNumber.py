import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0:
        #     return False
        # my_list = []
        # while x > 0:
        #     my_list.append(x % 10)
        #     x = x/10
        #
        # i = 0
        # j = len(my_list) - 1
        #
        # while i <= j:
        #     if my_list[i] != my_list[j]:
        #         return False
        #     else:
        #         i += 1
        #         j -= 1
        # return True

        # more optimized just check half of the nos

        # tmp = 0
        # pow = 0
        # while tmp < x:
        #
        #     tmp += (x %10) *10
        #     x = x/10

        if x < 0:
            return -1 * self.isPalindrome(-1 * x)
        tmp = x
        val = 0
        while tmp > 0:
            rem = tmp % 10
            val = val * 10 + rem
            tmp = tmp // 10

        if val > math.pow(2, 31) - 1:
            return 0
        return val


if __name__ == '__main__':
    soln = Solution()
    print(soln.isPalindrome(1534236469))
