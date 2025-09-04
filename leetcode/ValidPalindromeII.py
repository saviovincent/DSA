class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                # check both i+1,j-1
                tmp1 = s[i+1:j+1]
                tmp2 = s[i:j]
                return tmp1 == tmp1[::-1] or tmp2 ==tmp2[::-1]
            else:
                i += 1
                j -= 1

        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.validPalindrome("abcda"))
