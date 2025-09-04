class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minm = float('inf')
        for i in range(0, len(prices)):
            minm = min(minm, prices[i])  # minm so far
            profit = max(profit, prices[i] - minm)

        return profit


if __name__ == '__main__':
    soln = Solution()
    print(soln.maxProfit([7, 1, 5, 3, 6, 4]))
    print(soln.maxProfit([7, 6, 4, 3, 1]))
