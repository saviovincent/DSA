# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        j = n

        while i <= j:

            mid = (i + j) // 2
            bad_mid = isBadVersion(mid)
            bad_mid_1 = isBadVersion(mid-1)
            if bad_mid and not bad_mid_1:
                return mid
            elif bad_mid:
                j = mid - 1
            else:
                i = mid + 1

        return -1

if __name__ == '__main__':
    soln = Solution()
    print(soln.firstBadVersion(5))