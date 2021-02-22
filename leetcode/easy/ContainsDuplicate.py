class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp = set(nums)
        if len(tmp) < len(nums):
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([1, 7, 1]))
