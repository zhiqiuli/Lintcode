# APP2: DFS + Memoization. Memo:{(step, index), ways}
# Time: O(steps * min(arrLen, steps + 1)), Space: O(steps * min(arrLen, steps + 1)) 
# Result: Accepted 50%
class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def numWays(self, steps, arrLen):
        memo = {}
        return self.dfs(steps, arrLen, 0, memo) % (10 ** 9 + 7)
    
    def dfs(self, steps, arrLen, pos, memo):

        if (steps, pos) in memo:
            return memo[(steps, pos)]
        
        if pos < 0 or pos > arrLen - 1:
            memo[(steps, pos)] = 0
            return memo[(steps, pos)]
        
        if steps == 0:
            memo[(steps, pos)] = 1 if pos == 0 else 0
            return memo[(steps, pos)]

        memo[(steps, pos)] =   self.dfs(steps - 1, arrLen, pos - 1, memo) \
                             + self.dfs(steps - 1, arrLen, pos    , memo) \
                             + self.dfs(steps - 1, arrLen, pos + 1, memo) 

        return memo[(steps, pos)]

    
# APP3: DP. f[i][j]: total ways to get index j at ith step. ans = f[steps][0]. 
# f[i][j] = f[i - 1][j - 1] + f[i - 1][j] + f[i - 1][j + 1], f[0][0] = 1
# Time: O(steps * arrLen) Space: O(steps * arrLen) 
# Result: TLE when 430, 148488

# APP4: DP. Optimize APP3. If steps = 3, even arrLen = 400, max we can reach index = steps + 1
# So we can optimize arrLen = min(arrLen, steps + 1), just add one line to APP2
# Time: O(steps * min(arrLen, steps + 1)), Space: O(steps * min(arrLen, steps + 1)) 
# Result: Runtime: 30% Memory: 100%
class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def numWays(self, steps, arrLen):
        # Key
        # If steps = 3, even arrLen = 400, max we can reach index = steps + 1
        arrLen = min(arrLen, steps + 1)
        dp = [[0] * (arrLen + 2) for _ in range(steps + 1)]
        dp[0][1] = 1
        for i in range(1, steps + 1):
            for j in range(1, arrLen + 1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
        return dp[-1][1] % (10 ** 9 + 7)
