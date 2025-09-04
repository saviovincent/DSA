class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        ans = []
        while stack:
            ans.insert(0, stack.pop())
        return "".join(ans)


if __name__ == '__main__':
    soln = Solution()
    print(soln.removeStars("leet**cod*e"))
    print(soln.removeStars("erase*****"))
