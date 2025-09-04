class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        maps = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        stack = []

        for i in s:

            if i in maps:
                stack.append(i)

            else:
                if stack and i == maps[stack[len(stack) - 1]]:  # stack peek
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    soln = Solution()
    print(soln.isValid("[}"))
