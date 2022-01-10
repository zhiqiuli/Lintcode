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

