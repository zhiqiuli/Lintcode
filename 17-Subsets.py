# https://www.lintcode.com/problem/17/?_from=collection&fromId=161
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums = sorted(nums)
        res = []
        self.dfs(nums, [], res, 0)
        return res
    
    def dfs(self, nums, subset, res, start):
        res.append(subset[:])
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, subset, res, i + 1)
            subset.pop()
