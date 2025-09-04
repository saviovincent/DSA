class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        sets = set()
        for i in nums:
            if i in sets:
                return True
            else:
                sets.add(i)
        return False


if __name__ == '__main__':
    soln = Solution()
    print(soln.containsDuplicate([1, 2, 3, 1]))
