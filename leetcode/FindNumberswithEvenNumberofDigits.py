class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        even = 0
        for i in range(0, len(nums)):
            if self.digits(nums[i]) % 2 == 0:
                even += 1
        return even

    def digits(self, n):
        digit = 0
        while n > 0:
            n = n // 10
            digit += 1
        return digit


if __name__ == '__main__':
    soln = Solution()
    print(soln.findNumbers([12]))
