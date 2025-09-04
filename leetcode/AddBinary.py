class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if not len(a):
            return b
        elif not len(b):
            return a

        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        ans = ""

        while i >= 0 and j >= 0:
            summ = carry + int(a[i]) + int(b[j])
            if summ == 2:
                ans += '0'
                i -= 1
                j -= 1
                carry = 1
            elif summ == 3:
                ans += '1'
                i -= 1
                j -= 1
                carry = 1
            else:
                ans += str(summ)
                i -= 1
                j -= 1
                carry = 0

        while i >= 0:
            summ = carry + int(a[i])
            if summ == 2:
                ans += '0'
                i -= 1
                carry = 1
            elif summ == 3:
                ans += '1'
                i -= 1
                carry = 1
            else:
                ans += str(summ)
                i -= 1
                carry = 0

        while j >= 0:
            summ = carry + int(b[j])
            if summ == 2:
                ans += '0'
                j -= 1
                carry = 1
            elif summ == 3:
                ans += '1'
                j -= 1
                carry = 1
            else:
                ans += str(summ)
                j -= 1
                carry = 0

        if carry:
            ans += '1'
        return ans[::-1]


if __name__ == '__main__':
    soln = Solution()
    print(soln.addBinary("1010", "1011"))
