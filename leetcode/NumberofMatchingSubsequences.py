class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in words:
            check = self.isSubsequence(i,s)
            if check:
                count+=1
        return count
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i = j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1

        return i == len(s)

if __name__ == '__main__':
    soln = Solution()
    print(soln.numMatchingSubseq("dsahjpjauf",["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))