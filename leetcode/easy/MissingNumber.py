class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_sum = sum(nums)
        sum_nos = (len(nums) * (len(nums) + 1)) / 2

        return int(sum_nos - arr_sum)

    def xor_nos(self, nums):
        op1 = 0
        op2 = 0
        for i in range(0, len(nums) + 1):
            op1 = op1 ^ i
        for i in nums:
            op2 = op2 ^ i
        return op1 ^ op2


if __name__ == '__main__':
    soln = Solution()
    print(soln.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(soln.xor_nos([9, 6, 4, 2, 3, 5, 7, 0, 1]))
