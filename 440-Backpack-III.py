class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        dp = [0] * (m + 1)
        n = len(A)
        for i in range(n): # 注意顺序，先走n，再走m + 1
            for j in range(A[i], m + 1):
                if j - A[i] >= 0:
                    dp[j] = max(dp[j], # dp[j]可能已经存在，已经被之前的item计算过
                                dp[j - A[i]] + V[i]) # 考虑将i放入其中
        return dp[-1]
