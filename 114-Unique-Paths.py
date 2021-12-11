class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        res = [[0] * n for _ in range(m)]
        for i in range(n): res[0][i] = 1
        for j in range(m): res[j][0] = 1
        
        for j in range(1, m):
            for i in range(1, n):
                res[j][i] = res[j-1][i] + res[j][i-1]

        return res[-1][-1]
