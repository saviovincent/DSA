class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                count += 1
        if count % 2 == 0:
            return 1
        return -1


if __name__ == '__main__':
    soln = Solution()
    print(soln.arraySign([-1, 1, -1, 1, -1]))
