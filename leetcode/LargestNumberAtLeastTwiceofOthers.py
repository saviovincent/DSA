class Solution(object):

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxm = sec_maxm = -9999
        maxm_index = -1
        for i in range(0, len(nums)):
            if nums[i] > maxm:
                sec_maxm = maxm
                maxm = nums[i]
                maxm_index = i
            elif nums[i] > sec_maxm:
                sec_maxm = nums[i]

        if maxm >= 2 * sec_maxm:
            return maxm_index
        return -1


if __name__ == '__main__':
    soln = Solution()
    print(soln.dominantIndex([0, 0, 3, 2]))
