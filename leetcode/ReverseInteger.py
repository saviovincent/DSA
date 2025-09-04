import math


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        INT_MAX = 2147483647  # 2^31 - 1
        INT_MIN = -2147483648  # -2^31
        val = 0

        while x:
            rem = int(math.fmod(x, 10))
            x = int(x / 10)

            if val > INT_MAX // 10 or (val == INT_MAX // 10 and rem > 7):
                return 0
            elif val < INT_MIN // 10 or (val == INT_MIN // 10 and rem < 8):
                return 0

            val = val * 10 + rem  # should be post checking otherwise wrong ans for -2147483412

        return val


if __name__ == '__main__':
    soln = Solution()
    print(soln.reverse(-2147483412))
