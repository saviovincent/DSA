from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_map = OrderedDict()
        for i in s:
            if i in my_map:
                my_map[i] = my_map[i] + 1
            else:
                my_map[i] = 1

        for i in my_map:
            if my_map[i] == 1:
                return s.index(i)
        return -1


if __name__ == '__main__':
    soln = Solution()
    print(soln.firstUniqChar("leetcode"))
