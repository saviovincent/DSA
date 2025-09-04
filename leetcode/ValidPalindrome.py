import string


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # s = s.lower()
        # i = 0
        # j = len(s) - 1
        # stri = string.ascii_lowercase + "0123456789"
        #
        # maps = {}
        # for k in stri:
        #     maps[k] = 1
        #
        # while i < j:
        #     if s[i] in maps and s[j] in maps:
        #         if s[i] == s[j]:
        #             i = i + 1
        #             j = j - 1
        #         else:
        #             return False
        #     else:
        #         if s[i] not in maps:
        #             i = i + 1
        #         if s[j] not in maps:
        #             j = j - 1
        # return True

        str_to_check = ""
        maps = {
            'ltr': list(string.ascii_lowercase),
            'digit': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        }
        for i in s.lower():
            if i in maps['ltr'] or i in maps['digit']:
                str_to_check += i

        i = 0
        j = len(str_to_check) - 1

        while i < j:
            if str_to_check[i] != str_to_check[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.isPalindrome("0P"))
