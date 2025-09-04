class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        my_set = {"+", "-", "*", "/"}

        for i in tokens:
            if i not in my_set:
                stack.append(int(i))
            else:
                el1 = stack.pop()
                el2 = stack.pop()
                ans = None
                if i == "+":
                    stack.append(el2 + el1)
                elif i == "-":
                    stack.append(el2 - el1)
                elif i == "*":
                    stack.append(el2 * el1)
                elif i == "/":
                    stack.append(int(el2 / el1))
        return stack.pop()


if __name__ == '__main__':
    soln = Solution()
    print(soln.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    print(soln.evalRPN(["4", "13", "5", "/", "+"]))
