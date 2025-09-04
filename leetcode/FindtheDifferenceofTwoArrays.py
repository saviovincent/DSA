class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        maps1 = {}
        maps2 = {}
        rslt1 = set()
        rslt2 = set()

        for i in nums1:
            if i in maps1:
                maps1[i] += 1
            else:
                maps1[i] = 1

        for i in nums2:
            if i in maps2:
                maps2[i] += 1
            else:
                maps2[i] = 1

        for i in nums1:
            if i not in maps2:
                rslt1.add(i)
        for i in nums2:
            if i not in maps1:
                rslt2.add(i)

        return [list(rslt1), list(rslt2)]


if __name__ == '__main__':
    soln = Solution()
    print(soln.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
