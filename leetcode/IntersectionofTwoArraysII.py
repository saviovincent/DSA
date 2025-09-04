class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        maps = {}
        rslt = {}
        ans = []

        for i in nums1:
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1

        for i in nums2:
            if i in maps:

                if i not in rslt:
                    rslt[i] = 1
                else:
                    rslt[i] += 1

                maps[i] -= 1
                if maps[i] == 0:
                    del maps[i]
        for i in rslt:
            for j in range(0, rslt[i]):
                ans.append(i)

        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.intersect([1,2,2,1], [2,2]))
