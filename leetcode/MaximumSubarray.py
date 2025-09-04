class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # maxm = -9999
        # # i = j = 0
        # # for i in range(0, len(nums)):
        # #     sum = 0
        # #     for j in range(i, len(nums)):
        # #         sum = sum + nums[j]
        # #         maxm = max(maxm, sum)
        # # return maxm
        #
        # current_sum = 0
        # i = j = 0
        # max_sum = 0
        # all_negative = True
        # while j < len(nums):
        #     if nums[j] > 0:
        #         all_negative = False
        #     current_sum += nums[j]
        #     j += 1
        #     if current_sum < 0:
        #         i = j
        #         current_sum = 0
        #     else:
        #         max_sum = max(max_sum, current_sum)
        #
        # if all_negative:
        #     return max(nums)
        # return max_sum

        if not nums:
            return 0

        maxm = float('-inf')
        curr_sum = 0
        all_negative = True
        negative = float('-inf')

        for i in nums:

            # kadane needs atleast 1 positive to work
            if i > 0:
                all_negative = False
            else:
                negative = max(negative, i)

            curr_sum += i
            maxm = max(maxm, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        if all_negative:
            return negative
        return maxm


if __name__ == '__main__':
    soln = Solution()
    print(soln.maxSubArray([-3, -2, -1]))
