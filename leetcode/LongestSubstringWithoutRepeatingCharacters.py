class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = j = 0
        maps = {}
        ws = 0

        while j < len(s):

            if s[j] in maps:
                maps[s[j]] += 1
            else:
                maps[s[j]] = 1

            if j - i + 1 == len(maps):
                ws = max(ws, j - i + 1)

            elif j - i + 1 > len(maps):
                while j - i + 1 > len(maps):
                    maps[s[i]] -= 1
                    if maps[s[i]] == 0:
                        del maps[s[i]]
                    i += 1
            j += 1
        return ws


if __name__ == '__main__':
    soln = Solution()
    print(soln.lengthOfLongestSubstring("tmmzuxt"))
