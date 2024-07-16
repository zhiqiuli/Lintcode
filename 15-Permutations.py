from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums) # 如此定义访问过的元素可以保证去重
        self.dfs(nums, [], res, visited)
        return res
    
    def dfs(self, nums, perm, res, visited):
        # 递归出口
        if len(nums) == len(perm):
            res.append(perm[:])
        
        for i in range(len(nums)):
            # 跳过已经访问过的元素
            if visited[i]:
                continue
            # 经典dfs模版
            perm.append(nums[i])
            visited[i] = True
            self.dfs(nums, perm, res, visited)
            perm.pop()
            visited[i] = False
