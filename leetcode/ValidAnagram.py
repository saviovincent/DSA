class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # if len(s) != len(t):
        #     return False
        #
        # my_map = {}
        # for i in s:
        #     if i in my_map:
        #         my_map[i] = my_map[i] + 1
        #     else:
        #         my_map[i] = 1
        #
        # for i in t:
        #     if i in my_map:
        #         my_map[i] = my_map[i] - 1
        #         if my_map[i] == 0:
        #             del my_map[i]
        #     else:
        #         return False
        #
        # return len(my_map) == 0

        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in t:
            count[ord(i) - ord('a')] -= 1

        for i in count:
            if i > 0:
                return False
        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.isAnagram("anagram", "nagaram"))
