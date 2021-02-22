class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        maps = {'{': '}', '(': ')', '[': ']'}

        for i in s:
            if i in maps:
                stack.append(i)
            elif stack:
                if i is maps[stack[len(stack) - 1]]:
                    stack.pop()
                else:
                    return False
            # handle edge case
            elif (i is maps['{'] or i is maps['('] or i is maps['[']) and not stack:
                return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.isValid("()"))
