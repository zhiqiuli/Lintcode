'''
DP（前缀dp）

dp[i] 表示前i个“A”所用的最小步数

找到 i 能整除的最大的 j，然后一直黏贴，就能得到 i 个“A”了。也就是：
dp[i] = dp[j] + (i / j)

这里计算步数只加上(i/j)，是不是漏掉copy all的那一步？

并没有，因为一开始就有 j 个A了，所以我们只需要黏贴（i / j - 1）次，另外那一次就是copy all的那一步。

dp[i]是从小到大更新的，所以可以保证，当使用dp[j]时，它已经是得到 j 个A的最小步数了。
'''

class Solution:
    """
    @param n: The number of 'A'
    @return: the minimum number of steps to get n 'A'
    """
    def minSteps(self, n):
        if n == 1: return 0
        if n == 2: return 2
        dp = [0] * (n + 1)
        for i in range(3, n + 1):
            for j in range(i // 2, -1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + i // j
                    break
        return dp[-1]

      
      
      
