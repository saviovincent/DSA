from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        maps = defaultdict(list)
        for i in strs:
            count = [0] * 26

            for j in i:
                count[ord(j) - ord('a')] += 1
            maps[tuple(count)].append(i)

        return list(maps.values())

    #     if len(strs) == 0:
    #         return [[""]]
    #     else:
    #         result = {
    #             strs[0]: [strs[0]]
    #         }
    #
    #         for i in range(1, len(strs)):
    #             anagram_check = False
    #             for j in result:
    #                 if self.isAnagram(strs[i], j):
    #                     result[j].append(strs[i])
    #                     anagram_check = True
    #             if not anagram_check:
    #                 result[strs[i]] = [strs[i]]
    #
    #         arr = []
    #         for i in result:
    #             arr.append(result[i])
    #         return arr
    #
    # def isAnagram(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     my_map = {}
    #     for i in range(0, len(s)):
    #         if s[i] in my_map:
    #             my_map[s[i]] = my_map[s[i]] + 1
    #         else:
    #             my_map[s[i]] = 1
    #
    #     for i in range(0, len(t)):
    #         if t[i] in my_map:
    #             my_map[t[i]] = my_map[t[i]] - 1
    #         else:
    #             return False
    #
    #     for i in my_map:
    #         if my_map[i] != 0:
    #             return False
    #     return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
