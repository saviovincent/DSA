class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        stack = []

        def helper(open, closed, ans):
            if open == n and open == closed:
                ans.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                helper(open + 1, closed, ans)
                stack.pop()
            if closed < open:
                stack.append(")")
                helper(open, closed + 1, ans)
                stack.pop()
            return ans

        return helper(0, 0, [])


if __name__ == '__main__':
    soln = Solution()
    print(soln.generateParenthesis(3))
