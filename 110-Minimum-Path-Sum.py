class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        # f[i][j] = min(f[i-1][j], f[i][j-1]
        n, m = len(grid), len(grid[0])
        
        # status matrix
        f = [[0] * m for i in range(n)]

        f[0][0] = grid[0][0]
        for i in range(1, n):
            f[i][0] = grid[i][0] + f[i - 1][0]
        for j in range(1, m):
            f[0][j] = grid[0][j] + f[0][j - 1]

        for i in range(1, n):
            for j in range(1, m):
                f[i][j] = grid[i][j] + min(f[i-1][j], f[i][j-1])

        return f[-1][-1]
