class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def check(i, k):
            if i == len(nums):
                return True
            if nums[i] < nums[i - 1] and k == 0:
                return False

            if nums[i] < nums[i - 1] and k > 0:
                return check(i + 1, k - 1)
            return check(i + 1, k)

        return check(1, 1)


if __name__ == '__main__':
    soln = Solution()
    print(soln.checkPossibility([3, 4, 2, 3]))
