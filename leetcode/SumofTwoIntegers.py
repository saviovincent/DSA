class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        convert_to_32bit = 0xffffffff  # python uses >32bit to store integers
        while b & convert_to_32bit > 0:  # convert b to 32bit. Stop loop if b becomes negative
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        if b > 0:
            return a & convert_to_32bit
        return a


if __name__ == '__main__':
    soln = Solution()
    print(soln.getSum(-1, 1))
