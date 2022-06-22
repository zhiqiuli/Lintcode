from typing import (
    List,
)

class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def search_range(self, nums: List[int], target: int) -> List[int]:
        first = self.find_the_first (nums, target)
        last  = self.find_the_last  (nums, target)
        return [first, last]

    def find_the_first (self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target: return start
        if nums[end] == target: return end
        return -1
    
    def find_the_last (self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target: return end
        if nums[start] == target: return start
        return -1
