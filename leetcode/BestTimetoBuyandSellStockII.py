class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        for i in range(1, len(prices)):  # keep adding to profit for each day if profit > 0
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == '__main__':
    soln = Solution()
    print(soln.maxProfit([7, 1, 5, 3, 6, 4]))
