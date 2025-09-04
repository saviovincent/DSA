class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return
        i = 0
        j = count = len(nums) - 1
        result = [0] * (j + 1)

        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                result[count] = nums[j] * nums[j]
                j = j - 1
                count -= 1
            else:
                result[count] = nums[i] * nums[i]
                i = i + 1
                count -= 1
        return result


if __name__ == '__main__':
    soln = Solution()
    print(soln.sortedSquares([-4,-1,0,3,10]))
