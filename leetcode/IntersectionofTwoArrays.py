class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        maps = {}
        rslt = {}

        for i in nums1:
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1

        for i in nums2:
            if i in maps and i not in rslt:
                rslt[i] = 1

        return list(rslt.keys())


if __name__ == '__main__':
    soln = Solution()
    print(soln.intersection([4,9,5], [9,4,9,8,4]))
