class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        if len(s) == 0:
            return
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i = i + 1
            j = j - 1

        print(s)


if __name__ == '__main__':
    soln = Solution()
    soln.reverseString(['h','e'])
