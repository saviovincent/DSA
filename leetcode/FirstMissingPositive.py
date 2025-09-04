class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0

        while i < len(nums):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                self.swap(i, nums[i] - 1, nums)
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:  # i makes sure checking starts from 1
                return i + 1
        return len(nums) + 1

    def swap(self, a, b, nums):
        nums[a], nums[b] = nums[b], nums[a]


if __name__ == '__main__':
    soln = Solution()
    print(soln.firstMissingPositive([-1, -1, 1]))
