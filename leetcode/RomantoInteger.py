class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = 0
        for i in range(len(s),-1,-1):
            



if __name__ == '__main__':
    soln = Solution()
    print(soln.romanToInt("VX"))
