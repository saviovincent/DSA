class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        op = 0
        for i in nums:
            op = op ^ i
        return op


if __name__ == '__main__':
    soln = Solution()
    print(soln.singleNumber([4, 1, 2, 1, 2]))
