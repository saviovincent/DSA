class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(up, p, ans):
            if not up:
                ans.append(p)
                return
            for i in range(0, len(p) + 1):
                pre = p[:i]
                post = p[i:]
                new_list = list((pre + [up[0]] + post))
                helper(up[1:], new_list, ans)
            return ans

        return helper(nums, [], [])


if __name__ == '__main__':
    soln = Solution()
    print(soln.permute([1, 2, 3]))
