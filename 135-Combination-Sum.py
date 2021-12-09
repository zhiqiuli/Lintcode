# https://www.lintcode.com/problem/135/description?_from=collection&fromId=161

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates))) # 进行排序非常重要！
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, start, nums, res):
        # 递归出口 target <= 0
        if target < 0:
            return
        if target == 0:
            res.append(nums[:])
            return
        
        for i in range(start, len(candidates)):
            nums.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, nums, res)
            nums.pop()
