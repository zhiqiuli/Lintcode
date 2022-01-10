class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        if not prices:
            return 0
        if K > len(prices) // 2:
            return self.unlimited_profits(prices)
        buy  = [-prices[0]] * (K + 1)
        sell = [0] * (K + 1)
        for i in range(1, len(prices)):
            buy[0] = max(buy[0], sell[0] - prices[i]) # 假设i天开始第一次交易 同时也作为了边界条件
            for j in range(1, K + 1):
                buy[j]  = max(buy[j] , sell[j]  - prices[i])
                sell[j] = max(sell[j], buy[j-1] + prices[i])
        return max(sell)
    
    '''
    假设一共有 n 天, 那么这 n 天最多能够完成 n / 2 比交易, 也就是说, 当 k * 2 >= n 时, 就变成了 买卖股票的最佳时机 II, 反之, 我们可以作为动态规划问题解决:
    '''
    def unlimited_profits(self, prices):
        profits = 0
        closing = prices[0]
        for opening in prices:
            profits += opening - closing if opening > closing else 0
            closing = opening
        return profits


