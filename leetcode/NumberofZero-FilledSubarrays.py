class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = 0

        for i in nums:
            if i == 0:
                count += 1
            else:
                count = 0
            ans += count
        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.zeroFilledSubarray([0,0,0,2,0,0]))
