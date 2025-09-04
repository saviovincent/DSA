class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = right = 0
        jumps = 0

        while right < len(nums) -1 :
            max_jump = 0
            for i in range(left, right + 1):
                max_jump = max(max_jump, i + nums[i])
            left = right + 1
            right = max_jump
            jumps += 1
        return jumps


if __name__ == '__main__':
    soln = Solution()
    print(soln.jump([2, 3, 1, 1, 4]))
    print(soln.jump([1, 2, 0, 1, 4]))
