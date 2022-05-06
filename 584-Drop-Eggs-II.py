class Solution:
    """
    @param m: the number of eggs
    @param n: the number of floors
    @return: the number of drops in the worst case
    """
    def drop_eggs2(self, m: int, n: int) -> int:
        # 算法流程：
        # dp[i][j]表示当有i个鸡蛋，j层楼时，最少扔鸡蛋的次数（即答案值）
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 无论有多少个鸡蛋，在ground和第一层的答案都是固定的
        for i in range(1, m + 1):
            dp[i][0] = 0 # 在ground，不需要鸡蛋
            dp[i][1] = 1 # 在第一层，只需要一个鸡蛋
        
        # 一个鸡蛋的时候，只能从小到大尝试
        for j in range(1, n + 1):
            dp[1][j] = j
        
        # 递推式：
        # dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
        # k从1遍历到j，并且k的含义是第一个鸡蛋第一次从第k层往下扔时：
        # (1) 若碎了，那么只需要用剩下i-1个鸡蛋去确定在1到k-1层中的答案层即可
        # (2) 若没有碎，那么还有i个鸡蛋可用来确定k+1到j层中的答案层。因为所求扔鸡蛋次数需为最坏情况下的次数，故取上述两种情况的最大值加1用于更新dp[i][j]
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = sys.maxsize
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], \
                               1 + max(dp[i - 1][k - 1] , dp[i][j - k]))
        return dp[m][n]
