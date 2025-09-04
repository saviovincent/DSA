class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        def helper(up, p, ans):
            if not up:
                ans.append(p)
                return

            p1 = list(p)
            p2 = list(p)
            p1.append(up[0])
            helper(up[1:], p1, ans)
            helper(up[1:], p2, ans)

            return ans
        return helper(nums, [], [])


if __name__ == '__main__':
    soln = Solution()
    print(soln.subsets([1, 2]))
