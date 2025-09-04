class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        ans = ""
        while i < len(s):
            if s[i].isdigit() and int(s[i]) in range(1, 301):
                i, tmp = self.decode(s, i + 1, int(s[i]))
                ans += tmp
            else:
                ans += s[i]
                i += 1
        return ans

    def decode(self, s, i, times):
        tmp = ""
        queue = []
        i += 1
        while s[i] != "]":
            if s[i].isdigit() and int(s[i]) in range(1, 301):
                return self.decode(s, i + 1, int(s[i]))
            queue.append(s[i])
            i += 1
        return i + 1, str(times * "".join(queue))


if __name__ == '__main__':
    soln = Solution()
    print(soln.decodeString("2[a2[bc]]"))
