import math


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxm = sec_max = third_max = -math.inf

        for i in range(0, len(nums)):

            if nums[i] > maxm:
                third_max = sec_max
                sec_max = maxm
                maxm = nums[i]

            elif nums[i] > sec_max and nums[i] != maxm:
                third_max = sec_max
                sec_max = nums[i]

            elif nums[i] > third_max and nums[i] != maxm and nums[i] != sec_max:
                third_max = nums[i]

        if third_max != -math.inf:
            return third_max

        return maxm


if __name__ == '__main__':
    soln = Solution()
    print(soln.thirdMax([1, 2, -2147483648]))
