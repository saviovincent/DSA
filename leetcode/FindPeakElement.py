class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = len(nums) - 1
        mod = len(nums)

        if len(nums) == 1:
            return nums[0]

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] > nums[(mid + 1) % mod] and nums[mid] > nums[(mid - 1) % mod]:
                return nums[mid]
            elif nums[mid] < nums[(mid + 1) % mod]:
                i = mid + 1
            else:
                j = mid - 1
        return 0

if __name__ == '__main__':
    soln = Solution()
    print(soln.findPeakElement([2,1,2]))
