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
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1

        # self.recur(nums, target, 0, len(nums) -1)

    def recur(self, nums, target, l, h):

        if l > h: return -1
        mid = (l + h) // 2
        if nums[mid] is target:
            return mid
        elif nums[mid] < target:
            return self.recur(nums, target, mid + 1, h)
        else:
            return self.recur(nums, target, l, mid - 1)


if __name__ == '__main__':
    soln = Solution()
    soln.search([-1, 0, 3, 5, 9, 12], 9)
