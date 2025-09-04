class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i = 0
        # j = 1
        #
        # while j < len(nums):
        #     while j < len(nums) and nums[j] == nums[i]:
        #         j += 1
        #     if j < len(nums):
        #         nums[i + 1] = nums[j]
        #         i += 1
        #
        # return i + 1

        i = 0
        j = 1

        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        print(nums)
        return i + 1


if __name__ == '__main__':
    soln = Solution()
    print(soln.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
