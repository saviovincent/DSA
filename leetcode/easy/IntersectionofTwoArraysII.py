class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2) > len(nums1):
            return self.intersect(list(nums2), list(nums1))

        map = {}
        op = []
        for i in range(0, len(nums1)):
            if nums1[i] in map:
                map[nums1[i]] += 1
            else:
                map[nums1[i]] = 1

        for i in range(0, len(nums2)):
            if nums2[i] in map and map[nums2[i]] > 0:
                op.append(nums2[i])
                map[nums2[i]] -= 1
        return op


if __name__ == '__main__':
    soln = Solution()
    print(soln.intersect([2, 1], [1, 1]))
