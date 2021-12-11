# https://www.lintcode.com/problem/115/?_from=collection&fromId=161

class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        res  = [[0] * m for _ in range(n)]
        res[0][0] = 1

        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            else:
                res[i][0] = 1

        for j in range(m):
            if obstacleGrid[0][j] == 1:
                break
            else:
                res[0][j] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    continue
                res[i][j] = res[i-1][j] + res[i][j-1]
        
        return res[-1][-1]
