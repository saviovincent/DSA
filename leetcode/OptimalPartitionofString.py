class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """

        my_set = set()
        count = 1

        for i in range(len(s)):
            if s[i] in my_set:
                count += 1
                my_set = set()
                my_set.add(s[i])
            else:
                my_set.add(s[i])
        return count


if __name__ == '__main__':
    soln = Solution()
    print(soln.partitionString("abacaba"))
