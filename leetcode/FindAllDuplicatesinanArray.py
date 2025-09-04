class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        i = 0
        while i < len(nums):
            if nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                self.swap(i, nums[i] - 1, nums)
            else:
                i += 1

        duplicates = []
        for i in range(0, len(nums)):
            if i != nums[i] - 1:
                duplicates.append(nums[i])
        return duplicates

    def swap(self, i1, i2, arr):
        arr[i1], arr[i2] = arr[i2], arr[i1]


if __name__ == '__main__':
    soln = Solution()
    print(soln.findDuplicates([1, 1]))
