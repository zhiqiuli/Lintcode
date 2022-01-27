class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    # 方法1 - 记忆化搜索
    def maxCoins(self, nums):
        if not nums:
            return 0
        nums = [1, *nums, 1]
        return self.memo_search(nums, 0, len(nums) - 1, {})
    
    def memo_search(self, nums, i, j, memo):
        if i == j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        curr_max = 0
        # 保留i和j，burst之间的所有气球
        for k in range(i+1, j):
            left = self.memo_search(nums, i, k, memo)
            rite = self.memo_search(nums, k, j, memo)
            curr_max = max(curr_max, left + rite + nums[i] * nums[k] * nums[j])
        
        memo[(i, j)] = curr_max
        return curr_max

    
    
'''
上传侯卫东老师在算法强化班中的解法，区间型，区间长度from 3 to n。
初始化区间长度==2时，dp为0. 两个数相邻，没有中间的value，所以初始化成0.
'''
class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        if not nums:
            return 0
            
        nums = [1, *nums, 1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1): # length from 3 to n, inclusively
            for i in range(n + 1 - length):
                j = i + length - 1
                for k in range(i + 1, j): # k is between i and j, exclusively
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])
        
        return dp[0][-1]
