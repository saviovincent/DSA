class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(up, p, ans, target, added):
            if target < 0:
                return
            if target == 0:
                el = tuple(sorted(p))
                if el not in added:
                    ans.append(p)
                    added.add(el)
                return
            for i in up:
                p1 = list(p)
                p1.append(i)
                helper(up, p1, ans, target - i, added)
            return ans

        return helper(candidates, [], [], target, set())


if __name__ == '__main__':
    soln = Solution()
    print(soln.combinationSum([2, 3, 6, 7], 7))
