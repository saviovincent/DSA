class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return sorted(nums[0])

        arr1 = nums[0]
        arr2 = nums[1]
        maps = {}
        rslt = {}

        for i in arr1:
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1

        for i in arr2:
            if i in maps and i not in rslt:
                rslt[i] = 1

        rslt2 = rslt.copy()
        for i in range(2, len(nums)):
            for j in rslt2:
                if j not in nums[i]:
                    del rslt[j]

        return sorted(list(rslt.keys()))


if __name__ == '__main__':
    soln = Solution()
    print(soln.intersection([[3, 1, 2, 4, 5]]))
