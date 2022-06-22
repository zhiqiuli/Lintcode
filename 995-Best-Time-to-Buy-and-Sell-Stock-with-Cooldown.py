class Solution:
    """
    @param prices: a list of integers
    @return: return a integer
    """
    def maxProfit(self, prices):
        withShare = -prices[0]
        coolDown = 0
        noShare = 0
        for i in range(1, len(prices)):
            withShare = max(withShare, coolDown - prices[i]) # 当天withShare的话，(1)前一天同是withShare; (2)前一天coolDown并且当天买入
            coolDown  = max(coolDown, noShare)               # 当天coolDown的话，(1)前一天同是coolDown; (2)前一天noShare。coolDown的位置很重要，必须在withShare和noShare之间
            noShare   = max(noShare, withShare + prices[i])  # 当天noShare的话，(1)前一天同是noShare; (2)前一天withShare并且当天卖出
        return noShare

