class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # i = 0
        # j = len(nums) - 1
        # while i <= j:
        #     if nums[i] == val:  # need to remove
        #         if nums[j] != val:  # j not the element we want to remove
        #             nums[i], nums[j] = nums[j], nums[i]
        #             j -= 1
        #             i += 1
        #         else:
        #             while i <= j and nums[j] == val:  # j element we want to remove
        #                 j -= 1
        #             if i <= j:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 j -= 1
        #                 i += 1
        #     else:
        #         i += 1
        # print(nums)
        # return i

        i = 0
        j = len(nums) - 1

        while i <= j:

            if nums[i] != val:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1

        print(nums)
        return i


if __name__ == '__main__':
    soln = Solution()
    print(soln.removeElement([3, 2, 2, 3], 3))
