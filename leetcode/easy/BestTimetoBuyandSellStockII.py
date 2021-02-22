class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max += prices[i] - prices[i - 1]
        return max


if __name__ == '__main__':
    soln = Solution()
    print(soln.maxProfit([7, 1, 5, 3, 6, 4]))
