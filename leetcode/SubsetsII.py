class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        def helper(up, p, ans, added):
            if not up:
                el = tuple(sorted(p))
                if el not in added:
                    ans.append(p)
                    added.add(el)
                return

            p1 = list(p)
            p2 = list(p)
            p1.append(up[0])
            helper(up[1:], p1, ans, added)
            helper(up[1:], p2, ans, added)

            return ans

        return helper(nums, [], [], set())


if __name__ == '__main__':
    soln = Solution()
    print(soln.subsetsWithDup([1, 1]))
