class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rslt = 0

        for i in range(0, 32):
            bit = n & (1 << i)    # find ith bit set or not
            if bit > 0:
                rslt = rslt | (1 << 31 - i)  # set ith bit
        return rslt


if __name__ == '__main__':
    soln = Solution()
    print(soln.reverseBits(4294967293))
