###
### memoization search
###
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        return self.memo_search(0, len(A) - 1, {}, A)
    
    def memo_search(self, start, end, memo, A):
        if (start, end) in memo:
            return memo[(start, end)]

        if start >= end:
            return 0

        cost = sum(A[start:end + 1])
        minimum = sys.maxsize
        for mid in range(start, end):
            left  = self.memo_search(start  , mid, memo, A)
            right = self.memo_search(mid + 1, end, memo, A)
            minimum = min(minimum, left + right + cost)

        memo[(start, end)] = minimum
        return minimum

###
### dp
###
### key 1. state transit function
### key 2. how to do the loop
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        n = len(A)
        if n < 2:
            return 0

        # dp[i][j] => minimum cost merge from i to j
        dp = [[0] * n for _ in range(n)]

        # range_sum[i][j] => A[i] + A[i + 1] ... + A[j]
        range_sum = self.get_range_sum(A)

        # enumerate the range size first, start point second
        for length in range(2, n + 1): # shortest is 2 & longest is n
            for i in range(n + 1 - length): # consider length = n, i in range(1), then i = 0, so j = n - 1 >> perfect!
                j = i + length - 1
                dp[i][j] = sys.maxsize
                for k in range(i, j):
                    # left min + right min + the sum between i and j
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + range_sum[i][j])
        
        return dp[0][-1]

    def get_range_sum(self, A):
        dp = [[0] * len(A) for _ in range(len(A))]
        for i in range(len(A)):
            dp[i][i] = A[i]
            for j in range(i + 1, len(A)):
                dp[i][j] = dp[i][j - 1] + A[j]
        return dp
