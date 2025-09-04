class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        maxm = float('-inf')

        for i in nums:
            if i - 1 not in nums:
                j = i
                count = 0
                while j in nums:
                    count += 1
                    j += 1
                maxm = max(maxm, count)
        return maxm


if __name__ == '__main__':
    soln = Solution()
    print(soln.longestConsecutive([100, 4, 200, 1, 3, 2]))
