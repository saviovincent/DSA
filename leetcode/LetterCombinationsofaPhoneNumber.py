class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []
        maps = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def keypad(up, p, ans):
            if not up:
                ans.append(p)
                return
            for i in range(0, len(maps[up[0]])):
                keypad(up[1:], p + maps[up[0]][i], ans)
            return ans

        return keypad(digits, "", [])


if __name__ == '__main__':
    soln = Solution()
    print(soln.letterCombinations(""))
