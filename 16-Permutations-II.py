from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        visited = [False] * len(nums)
        self.dfs(nums, [], res, visited)
        return res

    def dfs(self, nums, path, res, visited):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            
            # remove the duplicated ones
            '''
            permutation去重

            存在相同时2'=2"，先挑前面的2'，再挑后面的2"。

            所以存在以下情况，return或break。

            nums    1 2' 2" 3
            visited x x  √  x
            '''
            if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                continue
            
            visited[i] = True
            path.append(nums[i])
            self.dfs(nums, path, res, visited)
            visited[i] = False
            path.pop()
