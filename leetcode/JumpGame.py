class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        idx_to_reach = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= idx_to_reach:
                idx_to_reach = i
        return idx_to_reach == 0



if __name__ == '__main__':
    soln = Solution()
    print(soln.canJump([2, 3, 1, 1, 4]))
    print(soln.canJump([3, 2, 1, 0, 4]))
    print(soln.canJump([0, 2, 3]))
