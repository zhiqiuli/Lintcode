'''
使用二维dp来定义前i个物品塞入容量为j的背包最满有多满。
首先处理corner case，就是物品总体积小于等于背包体积的时候，直接返回总体积就可以了。
然后使用转移方程，找到塞入第i个物品和不塞入第i个物品打擂台之后背包容量的最大值。
'''
class Solution:
    def backPack(self, m, A):
        n = len(A)
        if sum(A) <= m:
            return sum(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # dp[i][j] 前i件物品放入容量为j的背包中能获得的最大重量
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 此时第i件物品放不进去，注意i-1其实是第i个物品的意思
                if A[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 只考虑第i件物品的策略（放或不放）
                    # 如果不放第i件物品，那么问题就转化为“前i-1件物品放入容量为j的背包中”
                    dp[i][j] = max(dp[i - 1][j], 
                    # 如果放第i件物品，那么问题就转化为“前i-1件物品放入剩下的容量为j - A[i - 1]的背包中”。这个地方A[i - 1]其实相当于经典问题中的val[i - 1]
                                   dp[i - 1][j - A[i - 1]] + A[i - 1])
        return dp[n][m]
