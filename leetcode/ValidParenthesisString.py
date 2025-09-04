class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_min = left_max = 0

        for i in s:
            if i == "(":
                left_min += 1
                left_max += 1
            elif i == ")":
                left_min -= 1
                left_max -= 1
            elif i == "*":
                left_min -= 1
                left_max += 1

            if left_max < 0:
                return False
            if left_min < 0:    # left open has to be valid and cannot be < 0
                left_min = 0
        return left_min == 0


if __name__ == '__main__':
    soln = Solution()
    print(soln.checkValidString('(*))'))
    print(soln.checkValidString('(*)('))
