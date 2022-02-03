class Solution:
    """
    @param n: Your money
    @param prices: Cost of each university application
    @param probability: Probability of getting the University's offer
    @return: the  highest probability
    """
    def backpackIX(self, n, prices, probability):
        m  = len(prices)
        dp = [[1] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j - prices[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j],
                                   dp[i-1][j - prices[i-1]] * (1 - probability[i-1]))
        return 1.0 - dp[-1][-1]

    def backpackIX(self, n, prices, probability):
        m  = len(prices)
        dp      = [1] * (n + 1)
        dp_prev = dp[:]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j - prices[i-1] < 0:
                    dp[j] = dp_prev[j]
                else:
                    dp[j] = min(dp_prev[j],
                                dp_prev[j - prices[i-1]] * (1.0 - probability[i-1]))
            dp_prev = dp[:]
        return 1.0 - dp[-1]
