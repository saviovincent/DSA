from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not s or not t:
            return None
        maps = Counter(t)
        i = j = 0
        ans = ""
        count = len(maps.keys())

        while j < len(s):

            if s[j] in maps:
                maps[s[j]] -= 1
                if maps[s[j]] == 0:
                    count -= 1
            j += 1

            if count == 0:
                while count == 0:
                    if s[i] in maps:
                        if maps[s[i]] < 0:
                            maps[s[i]] += 1
                        elif maps[s[i]] == 0:
                            maps[s[i]] += 1
                            count += 1
                    i += 1
                if not ans:
                    ans = s[i - 1:j]
                elif j - i + 1 < len(ans):
                    ans = s[i - 1:j]
                # ans = min(ans, j - i + 1)
        return ans

if __name__ == '__main__':
    soln = Solution()
    print(soln.minWindow("toct",'toc'))