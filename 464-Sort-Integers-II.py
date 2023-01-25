from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a: List[int]):
        self.quick_sort(a, 0, len(a) - 1)

    def quick_sort(self, nums, start, end):
        
        if start >= end: return
        
        left, right = start, end
        # mid = (left + right) // 2
        pivot = nums[(left + right) // 2]

        while left <= right:
            
            while left <= right and nums[left] < pivot:
                left += 1
            
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)
