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

from typing import (
    List,
)

# 内容和前一版本一样，只是变量名不太一样
class Solution:
    """
    @param prices: a list of integers
    @return: return a integer
    """
    def max_profit(self, prices: List[int]) -> int:
        buy  = -prices[0]
        cool = 0
        sell = 0
        for i in range(1, len(prices)):
            buy  = max(buy , cool - prices[i]) # 如果买入 前一天肯定是cool
            cool = max(cool, sell)
            sell = max(sell, buy  + prices[i])
        return sell
