class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = []

        for i in range(len(temperatures) - 1, -1, -1):

            if not stack:
                stack.append((temperatures[i], i))
                ans.append(0)

            elif stack:

                temp, idx = stack[len(stack) - 1]
                if temp > temperatures[i]:
                    ans.append(idx - i)
                    stack.append((temperatures[i], i))

                else:
                    while stack and stack[len(stack) - 1][0] <= temperatures[i]:
                        stack.pop()

                    if stack:
                        temp, idx = stack[len(stack) - 1]
                        ans.append(idx - i)
                    else:
                        ans.append(0)
                    stack.append((temperatures[i], i))

        ans.reverse()
        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
