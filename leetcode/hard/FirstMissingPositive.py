class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)

        if n == 0:
            return 1

        while i < n:
            if nums[i] != i and 0 < nums[i] < n:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i = i + 1

        for i in range(1, n+1):
            if i == n:
                return i
            elif i != nums[i]:
                return i


if __name__ == '__main__':
    soln = Solution()
    print(soln.firstMissingPositive([0,1,2]))
