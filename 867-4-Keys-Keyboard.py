'''
动态规划，建立n+1的dp,初始赋值dp[i] = i,即全部用key1。转移方程dp[i] = max(dp[i], dp[prev] * count)；其中prev取值i-3到1；
每次prev减一，count加一，因为key4(ctrl-v)可以直接复制buffer里的数。返回dp[N]
时间O(n^2), 空间O(n)。
'''
class Solution:
    """
    @param N: an integer
    @return: return an integer
    """
    def maxA(self, N):
        dp = [i for i in range(N + 1)]
        
        for i in range(4, N+1):
            prev  = i - 3 # 跳过key1, key2, key3
            count = 2 # key4 1次 2，key4 2次 3
            while prev > 0:
                dp[i] = max(dp[i], dp[prev]*count)
                prev  -= 1
                count += 1
        return dp[N]
