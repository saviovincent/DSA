class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        len_arr = []
        for i in strs:
            len_arr.append(len(i))

        loop = min(len_arr)
        if loop == 0:
            return

        unique = set()
        ans = ""

        for i in range(0, loop):
            for j in range(0, len(strs)):
                unique.add(strs[j][i])
            if len(unique) > 1:
                break
            else:
                ans += unique.pop()
        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.longestCommonPrefix(["flower", "flower", "flower", "flower"]))
