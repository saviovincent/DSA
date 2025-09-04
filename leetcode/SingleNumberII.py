class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0
        for i in range(32):
            count = 0
            mask = 1 << i

            for j in nums:
                if j & mask:
                    count += 1
            if count % 3 != 0:
                ans = ans | mask

        """
        The below line checks to see if the sign bit is set, and takes the two's compliment with a 32 bit mask if it is.
        This is necessary in python because integers are not locked to n bits, they grow dynamically.
        Python does not know if the answer we constructed is in two's compliment or not without us explicitly telling it
        where the sign bit is.
        """

        if ans & 1 << 31:
            ans = -((~ans + 1) & 0xffffffff)
        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))
