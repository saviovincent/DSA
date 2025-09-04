class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        i = 0
        j = len(nums) - 1
        mod = len(nums)

        while i <= j:

            mid = (i + j) // 2

            if nums[mid] < nums[(mid + 1) % mod] and nums[mid] < nums[(mid - 1) % mod]:
                return nums[mid]
            elif nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid - 1


if __name__ == '__main__':
    soln = Solution()
    print(soln.findMin([2, 2, 2, 0, 1]))
