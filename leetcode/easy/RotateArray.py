class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        k = k % len(nums)
        for i in range(0, k):
            nums.insert(0, nums.pop())
        return nums


if __name__ == '__main__':
    soln = Solution()
    print(soln.rotate([1, 2, 3, 4, 5, 6, 7], 3))
