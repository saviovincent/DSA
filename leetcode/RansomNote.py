class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        map = {}
        for i in magazine:
            if i in map:
                map[i] = map[i] + 1
            else:
                map[i] = 1

        for i in ransomNote:
            if i in map:
                map[i] = map[i] - 1
            else:
                return False
        for i in map:
            if map[i] < 0:
                return False
        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.canConstruct("", ""))
