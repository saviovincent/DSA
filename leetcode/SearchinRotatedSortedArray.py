class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i = 0
        j = len(nums) - 1

        while i <= j:

            mid = (i + j) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:

                if nums[i] > nums[mid]:  # unsorted
                    j = mid - 1

                else:
                    i = mid + 1
            elif nums[mid] < target:

                if nums[mid] < nums[j]:  # unsorted
                    i = mid + 1

                else:
                    j = mid - 1
        return -1


if __name__ == '__main__':
    soln = Solution()
    print(soln.search([4, 5, 6, 7, 0, 1, 2], 0))
