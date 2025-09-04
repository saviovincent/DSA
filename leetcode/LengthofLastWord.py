class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                if count == 0:
                    continue
                else:
                    break

            else:
                count+=1

        return count

if __name__ == '__main__':
    soln = Solution()
    print(soln.lengthOfLastWord("a"))