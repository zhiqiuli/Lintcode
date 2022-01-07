https://www.lintcode.com/problem/41/description

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        f = [0] * len(nums) # 状态转移方程 f[i]代表必须使用nums[i]时的最大值
        f[0] = nums[0]
        for i in range(1, len(nums)):
            if f[i - 1] < 0:
                f[i] = nums[i] # 前面的最大值总是负的 所以不如直接使用nums[i]
            else:
                f[i] = f[i - 1] + nums[i]
        return max(f)
    
    
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # maxSubArray ended @ i -> dp[i]
        dp = nums[:]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
        return max(dp)
