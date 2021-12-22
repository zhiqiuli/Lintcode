https://www.lintcode.com/problem/975/description
  
class Solution:
    """
    @param n: The number of 'A'
    @return: the minimum number of steps to get n 'A'
    """
    def minSteps(self, n):
        if n <= 1:
            return 0
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[2] = 2
        for i in range(3, n + 1):
            for j in range(i // 2, -1, -1):
                if i % j == 0:
                    dp[i] = (i // j) + dp[j]
                    break
        return dp[-1]
