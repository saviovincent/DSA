class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        arr = s.strip().split()
        rslt = ""

        for i in range(0, len(arr)):
            tmp = list(arr[i])
            k = 0
            j = len(tmp) - 1
            while k < j:
                tmp[k], tmp[j] = tmp[j], tmp[k]
                k += 1
                j -= 1
            tmp = "".join(tmp)
            rslt += tmp + " "

        return rslt.


if __name__ == '__main__':
    soln = Solution()
    print(soln.reverseWords("Let's take LeetCode contest"))
