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
            withShare = max(withShare, coolDown - prices[i]) # 前一天withShare或者coolDown
            coolDown = max(coolDown, noShare) # coolDown的位置很重要 必须在withShare和noShare之间
            noShare = max(noShare, withShare + prices[i])
        return noShare

