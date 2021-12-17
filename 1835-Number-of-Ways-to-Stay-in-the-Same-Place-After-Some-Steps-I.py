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
