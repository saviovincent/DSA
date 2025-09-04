class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i = j = 0
        ans = ""
        flip = 0

        while i < len(word1) and j < len(word2):
            if flip & 1 == 0:
                ans += word1[i]
                flip = 1
                i += 1
            else:
                ans += word2[j]
                flip = 0
                j += 1

        if i < len(word1):
            ans += word1[i:]
        if j < len(word2):
            ans += word2[j:]

        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.mergeAlternately("ab", "pqrs"))
