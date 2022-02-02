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
