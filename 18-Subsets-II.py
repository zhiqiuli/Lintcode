# https://www.lintcode.com/problem/18/description?_from=collection&fromId=161
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums = sorted(nums)
        res = []
        self.dfs(nums, res, 0, [])
        return res
    
    def dfs(self, nums, res, start, chars):

        res.append(chars[:])

        for i in range(start, len(nums)):
            # 剪枝 去重
            if i > start and nums[i] == nums[i - 1]:
                continue
            chars.append(nums[i])
            self.dfs(nums, res, i + 1, chars)
            chars.pop()
