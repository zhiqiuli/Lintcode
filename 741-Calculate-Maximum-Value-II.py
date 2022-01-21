'''
dp[i][j]表示第i個到第j個substring之最大值

初始化

dp[i][i] = str[i]

dp[i][i + 1] = max(str[i] * str[i + 1], str[i] + str[i + 1])

方程式

dp[i][j] = max(dp[i][k] + dp[k + 1][j], dp[i][k] * dp[k + 1][j]), i <= k < j
'''
class Solution:
    """
    @param str: a string of numbers
    @return: the maximum value
    """
    def maxValue(self, str):
        n = len(str)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = int(str[i])
        for length in range(2, n + 1):
            for i in range(n): # or you can do "for left in range(len(str) - length + 1)"
                j = i + length - 1
                if j > n - 1:
                    break
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + dp[k + 1][j],
                                   dp[i][k] * dp[k + 1][j])
        return dp[0][-1]
