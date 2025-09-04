# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 0
        j = n

        while i <= j:

            mid = (i + j) // 2
            guess = guess(mid)
            if guess == 0:
                return mid
            elif guess == -1:
                j = mid - 1
            else:
                i = mid + 1

        return -1


if __name__ == '__main__':
    soln = Solution()
    print(soln.guessNumber(5))
