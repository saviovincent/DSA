class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_sum = sum(nums)
        sum_nos = (len(nums) * (len(nums) + 1)) / 2

        return int(sum_nos - arr_sum)


if __name__ == '__main__':
    soln = Solution()
    print(soln.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
