class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # l = [1] * len(nums)
        # r = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     l[i] = l[i - 1] * nums[i - 1]
        # for i in range(len(nums) - 2, -1, -1):
        #     r[i] = r[i + 1] * nums[i + 1]

        ans = [1] * len(nums)

        prefix = 1
        for i in range(0, len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.productExceptSelf([1, 2, 3, 4]))
