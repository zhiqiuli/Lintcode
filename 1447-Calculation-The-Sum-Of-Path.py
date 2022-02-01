分成4段做dp，0->1->2->3->4，然后最终结果相乘

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l: The length of the matrix
    @param w: The width of the matrix
    @param points: three points 
    @return: The sum of the paths sum
    """
    def calculationTheSumOfPath(self, l, w, points):
        points = sorted([(0, 0)] + [(p.x-1, p.y-1) for p in points] + [(l-1, w-1)])
        MOD = 10**9 + 7
        total = 1
        n = len(points)
        
        for i in range(1, n):
            # KEY
            # (0, 0)->(1, 1) OK
            # (2, 1)->(1, 2) impossible then return 0
            if points[i][1] < points[i-1][1]:
                return 0
            total = total * self.numPath(points[i-1], points[i])
            total = total % MOD
        
        return total
    

    def numPath(self, start, end):
        w, l = end[0] - start[0] + 1, end[1] - start[1] + 1
        dp = [[0] * w for _ in range(l)]
        for i in range(l):
            dp[i][0] = 1
        for j in range(w):
            dp[0][j] = 1
        for i in range(1, l):
            for j in range(1, w):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
