class Solution(object):

    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        summ = sum(nums)
        left_sum = 0
        right_sum = summ - nums[0]
        i = 0
        n = len(nums)

        while i < n:

            if right_sum == left_sum:
                return i
            else:
                left_sum += nums[i]
                if i+1 == n:
                    right_sum = 0
                else:
                    right_sum -= nums[i+1]
                i += 1
        return -1


if __name__ == '__main__':
    soln = Solution()
    print(soln.pivotIndex([-1,-1,0,1,1,0]))
