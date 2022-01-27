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
        for k in range(i+1, j):
            left = self.memo_search(nums, i, k, memo)
            rite = self.memo_search(nums, k, j, memo)
            curr_max = max(curr_max, left + rite + nums[i] * nums[k] * nums[j])
        
        memo[(i, j)] = curr_max
        return curr_max
