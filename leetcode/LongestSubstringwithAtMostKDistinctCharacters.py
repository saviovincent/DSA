class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = j = 0
        my_map = {}
        # k = 2
        ws = 0

        while j < len(s):

            # calc
            if s[j] in my_map:
                my_map[s[j]] += 1
            else:
                my_map[s[j]] = 1

            # check <k cond.
            if len(my_map) < k:
                ws = max(ws, j - i + 1)
                j += 1

            # check ==k cond.
            elif len(my_map) == k:
                ws = max(ws, j - i + 1)
                j += 1

            # check >k cond.
            elif len(my_map) > k:
                while len(my_map) > k:
                    my_map[s[i]] -= 1
                    if my_map[s[i]] == 0:
                        my_map.pop(s[i])
                    i += 1
                j += 1
        return ws


if __name__ == '__main__':
    soln = Solution()
    print(soln.lengthOfLongestSubstringKDistinct("eceba", 2))
