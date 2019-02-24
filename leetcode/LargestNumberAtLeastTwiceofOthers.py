class Solution(object):

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxm = max(nums)

        flag = False

        for i in nums:
            if maxm < 2*i and i != maxm:
                flag = True
            else:
                continue

        if not flag:
            return nums.index(maxm)
        else:
            return -1