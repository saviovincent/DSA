class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # brute force
        # max_profit = 0
        # for i in range(0, len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] - prices[i] > 0 and prices[j] - prices[i] > max_profit:
        #             max_profit = prices[j] - prices[i]
        # return max_profit

        min = 100000
        max = 0

        for i in range(0, len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > max:
                max = prices[i] - min
        return max


if __name__ == '__main__':
    soln = Solution()
    print(soln.maxProfit([7, 1, 5, 3, 6, 4]))
