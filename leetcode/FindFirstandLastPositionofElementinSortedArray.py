class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.first(nums, target)
        last = self.last(nums, target)
        return [first, last]

    def first(self, nums, target):

        i = 0
        j = len(nums) - 1
        pos = -1

        while i <= j:

            mid = (i + j) // 2
            if nums[mid] == target:
                pos = mid
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return pos

    def last(self, nums, target):

        i = 0
        j = len(nums) - 1
        pos = -1

        while i <= j:

            mid = (i + j) // 2
            if nums[mid] == target:
                pos = mid
                i = mid + 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return pos


if __name__ == '__main__':
    soln = Solution()
    print(soln.searchRange([5, 7, 7, 8, 8, 10], 6))
