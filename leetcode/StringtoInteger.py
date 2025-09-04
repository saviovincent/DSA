import math


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        i = 0
        neg = False
        ans = ""
        vals = {str(i) for i in range(0, 10)}

        while i < len(s):
            if s[i] == '-':
                neg = True
                i += 1
                continue
            elif s[i] == '+':
                i += 1
                continue

            if s[i] in vals:
                ans += s[i]
            else:
                if ans:
                    i = len(s)
                else:
                    break

            i += 1

        if not ans:
            return 0

        ans = int(ans)
        if ans < math.pow(-2, 31):
            ans = math.pow(2, 31)
        elif ans > math.pow(2, 31):
            ans = math.pow(2, 31)

        if neg:
            return -1 * int(ans)
        return int(ans)


if __name__ == '__main__':
    soln = Solution()
    print(soln.myAtoi("+1"))
