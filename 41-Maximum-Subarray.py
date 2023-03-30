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


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def max_sub_array(self, nums: List[int]) -> int:
        final_res = res = nums[0]
        for num in nums[1:]:
            # option 1
            if res < 0:
                res = num # 如果前一步的结果是负数，则直接使用num
            else:
                res += num
            # option 2
            # res = max(num, res + num) # 如果前一步的结果是负数，则直接使用num
            final_res = max(final_res, res)
        return final_res
