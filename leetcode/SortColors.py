class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        lt = curr = 0
        gt = len(nums) - 1

        while curr <= gt:

            if nums[curr] == 0:
                nums[lt], nums[curr] = nums[curr], nums[lt]
                lt += 1
                curr += 1
            elif nums[curr] == 2:
                nums[gt], nums[curr] = nums[curr], nums[gt]
                gt -= 1
            else:
                curr += 1

        return nums

if __name__ == '__main__':
    soln = Solution()
    print(soln.sortColors([2, 0, 2, 1, 1, 0]))
