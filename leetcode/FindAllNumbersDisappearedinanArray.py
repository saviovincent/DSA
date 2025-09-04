class Solution(object):
    def findDisappearedNumbers(self, nums):
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

        missing = []
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                missing.append(i + 1)
        return missing

    def swap(self, a, b, nums):
        nums[a], nums[b] = nums[b], nums[a]


if __name__ == '__main__':
    soln = Solution()
    print(soln.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
