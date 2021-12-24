class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # dp[i] 在i位置上的LIS长度是多少
        # dp[i+1]=dp[i]+1 if A[i+1] > A[i] else dp[i+1]=1
        if not A:
            return 0
        lic, ldc, max_len = 1, 1, 1 # 在i处的最长的增序列/降序列
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                lic += 1
                ldc  = 1
            elif A[i] < A[i - 1]:
                ldc += 1
                lic  = 1
            else:
                lic  = 1
                ldc  = 1
            max_len = max(lic, ldc, max_len)
        return max_len
