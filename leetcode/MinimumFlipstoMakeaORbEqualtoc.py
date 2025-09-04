class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        tmp1 = a | b
        tmp2 = tmp1 ^ c

        count = 0
        while tmp2 > 0:
            tmp2 = tmp2 & tmp2-1
            count +=1
        return count

if __name__ == '__main__':
    soln = Solution()
    print(soln.minFlips(2,6,5))