class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        my_map = {}
        arr = s.split(" ")

        if len(pattern) != len(arr):
            return False

        for i in zip(pattern,arr):
            if i[0] in my_map:
                if i[1] != my_map[i[0]]:
                    return False
            else:
                if i[1] not in my_map.values():
                    my_map[i[0]] = i[1]
                else:
                    return False
        return True

if __name__ == '__main__':
    soln = Solution()
    print(soln.wordPattern("aaa","aa aa aa aa"))