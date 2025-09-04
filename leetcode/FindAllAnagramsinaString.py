class Solution(object):
    def findAnagrams(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s2) < len(s1):
            return self.findAnagrams(s2, s1)

        maps = {}
        for i in s1:
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1
        ans = []
        j = 0
        while j < len(s2):
            if s2[j] in maps:
                # check continuous
                permute = self.check_permute(s2, maps, j, s1)
                if permute:
                    ans.append(j)
            j += 1
        return ans

    def check_permute(self, s2, s1_map, j, s1):
        s11_map = s1_map.copy()
        for i in range(0, len(s1)):
            if j < len(s2) and s2[j] in s11_map:
                s11_map[s2[j]] -= 1
                if s11_map[s2[j]] == 0:
                    del s11_map[s2[j]]
                if len(s11_map) == 0:
                    return True
                j += 1
            else:
                break
        return False


if __name__ == '__main__':
    soln = Solution()
    print(soln.findAnagrams("abab", "ab"))
