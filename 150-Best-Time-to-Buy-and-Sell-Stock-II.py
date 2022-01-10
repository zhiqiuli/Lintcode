class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices: return 0

        '''
        # 在i天存在两种状态，有股票或没有股票，分别在买入之后和卖出之后
        dp0 = [ 0 ] * len(prices) # max profit如果没有股票 aka 卖出之后没有股票
        dp1 = [ 0 ] * len(prices) # max profit如果有股票 aka 买入之后有股票
        dp1[0] = -prices[0]
        '''

        noShare   = 0
        withShare = -prices[0]

        for i in range(1, len(prices)):
            '''
            dp0[i] = max(dp0[i - 1], dp1[i - 1] + prices[i]) # 之前有股票，今天卖出
            dp1[i] = max(dp1[i - 1], dp0[i - 1] - prices[i] ) # 之前没股票，今天买入
            '''
            
            # withShare/noShare的顺序没有关系 但是最好根据buy/sell顺序
            withShare = max(withShare, noShare   - prices[i])
            noShare   = max(noShare  , withShare + prices[i])

        return noShare

