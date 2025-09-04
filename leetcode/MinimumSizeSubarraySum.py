class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        i = j = 0
        summ = 0
        ws = 1000000

        while j < len(nums):
            summ += nums[j]
            if summ < target:
                j += 1
            elif summ >= target:
                while summ >= target:
                    summ -= nums[i]
                    ws = min(j - i + 1, ws)
                    i += 1
                j += 1
        if ws == 1000000:
            return 0
        return ws


if __name__ == '__main__':
    soln = Solution()
    print(soln.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
