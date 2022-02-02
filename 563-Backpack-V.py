'''
算法思路
题目说物品只能使用一次和求方案数，可以看出这题的模型是01背包

我们定义状态dp[i][j] 来表示前i个物品重量有多少种方式组出重量j

状态转移方程为：

  当不放第i个物品时 ： dp[i][j] = dp[i - 1][j] 

  当放第i个物品时：dp[i][j] += dp[i - 1][j - nums[i - 1]] 
'''
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        # dp[i][j] - there are dp[i][j] ways to fill a bag with size j with first i items
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
    
    
    
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        dp_prev = dp[:]
        for i in range(1, n + 1):
            for j in range(1, target + 1):
            	if j >= nums[i-1]:
            		dp[j] = dp[j] + dp_prev[j-nums[i-1]]
            dp_prev = dp[:]
        return dp_prev[-1]
