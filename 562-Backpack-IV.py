# 标准无穷背包
class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for j in range(num, target + 1):
                dp[j] = dp[j] + dp[j - num]
        return dp[-1]
