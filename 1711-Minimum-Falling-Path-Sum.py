###
### Method 1. DP with 2d array
###
class Solution:
    """
    @param A: the given array
    @return: the minimum sum of a falling path
    """
    def minFallingPathSum(self, A):
        m, n = len(A), len(A[0])
        dp = [[0] * n for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(n):
                left_top  = dp[i-1][max(j-1,0)]
                right_top = dp[i-1][min(j+1,n-1)]
                dp[i][j] = A[i-1][j] + min(left_top, right_top, dp[i-1][j])
        return min(dp[-1])


###
### Method 2. DP with 1d array
###
class Solution:
    """
    @param A: the given array
    @return: the minimum sum of a falling path
    """
    def minFallingPathSum(self, A):
        m, n = len(A), len(A[0])
        dp      = [0] * n
        dp_prev = dp[:]
        for i in range(m):
            for j in range(n):
                left_top  = dp_prev[max(j-1,0)]
                right_top = dp_prev[min(j+1,n-1)]
                dp[j]     = A[i][j] + min(left_top, right_top, dp_prev[j])
            dp_prev = dp[:]
        return min(dp_prev)
