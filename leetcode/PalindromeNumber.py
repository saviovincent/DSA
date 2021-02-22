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

        #more optimized just check half of the nos

        # tmp = 0
        # pow = 0
        # while tmp < x:
        #
        #     tmp += (x %10) *10
        #     x = x/10


if __name__ == '__main__':
    soln = Solution()
    print soln.isPalindrome(-12344323)
