class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        op1 = 0
        for i in nums:
            op1 = op1 ^ i
        return op1


if __name__ == '__main__':
    soln = Solution()
    print(soln.singleNumber([4,1,2,1,2]))