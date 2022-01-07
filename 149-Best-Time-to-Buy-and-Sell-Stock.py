class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        lowest     = prices[0]
        max_profit = 0
        for p in prices[1:]:
            max_profit = max(p - lowest, max_profit)
            lowest     = min(lowest, p)
        return max_profit
