from typing import (
    List,
)

class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """
    def twoSumVII(self, nums: List[int], target: int) -> List[List[int]]:
        
        def ascending():
            lo = min(range(len(nums)), key=nums.__getitem__)
            for i in range(lo, -1, -1):
                if nums[i] <= 0: # 0必定是排在第一的，将0考虑在这个部分
                    yield i
            for i in range(1, len(nums)):
                if nums[i] > 0:
                    yield i
        
        def descending():
            hi = max(range(len(nums)), key=nums.__getitem__)
            for i in range(hi, -1, -1):
                if nums[i] >= 0:
                    yield i
            for i in range(1, len(nums)):
                if nums[i] < 0:
                    yield i
        
        up, down, out = ascending(), descending(), []
        i, j = next(up), next(down)
        while nums[i] < nums[j]:
            if nums[i] + nums[j] > target:
                j = next(down)
            elif nums[i] + nums[j] < target:
                i = next(up)
            else:
                out.append([min(i, j), max(i, j)])
                j = next(down)
                i = next(up)
        
        return out
