'''
https://www.lintcode.com/problem/151/solution/56574

无论题目中是否允许「在同一天买入并且卖出」这一操作，最终的答案都不会受到影响，这是因为这一操作带来的收益为零。
'''

from typing import (
    List,
)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def max_profit(self, prices: List[int]) -> int:
        # write your code here
        if not prices: return 0
        buy1, buy2   = -prices[0], -prices[0]
        sell1, sell2 = 0, 0
        for i in range(1, len(prices)):
            buy1  = max(buy1  ,        - prices[i]) # 在i位置第一次buy。想要cost最小，所以总是选最小值，此处等价于min()。
                                                    # 此处存在先后顺序，只有存在buy才会有sell。
            sell1 = max(sell1 ,  buy1  + prices[i]) # 在i位置第一次sell。想要profit最大。
            buy2  = max(buy2  ,  sell1 - prices[i]) 
            sell2 = max(sell2 ,  buy2  + prices[i])
        return sell2 # 只需要return sell2即可，sell2包含了sell1的profit
