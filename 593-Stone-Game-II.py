class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame2(self, A):
        
        circle_len = len(A) # define the circle length
        if circle_len < 2:
            return 0
        
        A = A + A

        # dp[i][j] => minimum cost merge from i to j
        dp = [[0] * len(A) for _ in range(len(A))]

        # range_sum[i][j] => A[i] + A[i + 1] ... + A[j]
        range_sum = self.get_range_sum(A)

        # enumerate the range size first, start point second
        for length in range(2, circle_len + 1): # shortest is 2 & longest is still circle_len
            for i in range(len(A) + 1 - length): # consider length = n, i in range(1), then i = 0, so j = n - 1 >> perfect!
                j = i + length - 1
                dp[i][j] = sys.maxsize
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], \
                                   dp[i][k] + dp[k + 1][j] + range_sum[i][j])
        
        ans = sys.maxsize
        for left in range(circle_len):
            ans = min(ans, dp[left][left + circle_len - 1])
            
        return ans

    def get_range_sum(self, A):
        range_sum = [[0] * len(A) for _ in range(len(A))]
        for i in range(len(A)):
            range_sum[i][i] = A[i]
            for j in range(i + 1, len(A)):
                range_sum[i][j] = range_sum[i][j - 1] + A[j]
        return range_sum
