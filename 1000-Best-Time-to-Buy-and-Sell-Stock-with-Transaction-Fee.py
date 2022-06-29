class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def max_profit(self, prices: List[int], fee: int) -> int:
        buy  = -prices[0]
        sell = 0
        for i in range(1, len(prices)):
            buy  = max(buy , sell - prices[i]      ) # 继续持有 或者 买入prices[i]，此时会消耗之前的sell profit
            sell = max(sell, buy  + prices[i] - fee) # 继续空仓 或者 卖出prices[i]，此时profit会有fee
        return sell

class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, prices, fee):
        if not prices: return 0
        withShare = -prices[0]
        noShare   = 0
        for i in range(1, len(prices)):
            withShare = max(withShare, noShare   - prices[i])
            noShare   = max(noShare  , withShare + prices[i] - fee)
        return noShare

