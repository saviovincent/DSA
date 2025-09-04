class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0

        while i < len(nums):
            if nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                self.swap(i, nums[i] - 1, nums)
            else:
                i += 1
        # return nums

        missing = None
        dup = None
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                missing = (i + 1)
                dup = nums[i]
        return [dup, missing]

    def swap(self,a, b, nums):
        nums[a], nums[b] = nums[b], nums[a]


if __name__ == '__main__':
    soln = Solution()
    print(soln.findErrorNums([1, 2, 2, 4]))
