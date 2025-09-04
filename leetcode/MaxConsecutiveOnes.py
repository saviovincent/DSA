class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = j = maxm = 0
        while j < len(nums):
            if nums[j] == 0:
                i = j = j + 1
            else:
                j += 1
            maxm = max(maxm, (j - 1) - i + 1)
        return maxm


if __name__ == '__main__':
    soln = Solution()
    print(soln.findMaxConsecutiveOnes([0,0,0]))
