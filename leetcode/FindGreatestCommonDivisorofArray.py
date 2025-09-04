class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxm = max(nums)
        minm = min(nums)
        return self.gcd(maxm, minm)

    def gcd(self, a, b):
        if a % b == 0:
            return b
        return self.gcd(b, a % b)


if __name__ == '__main__':
    soln = Solution()
    # print(soln.gcd(5, 10))
    print(soln.findGCD([2,5,6,9,10]))
