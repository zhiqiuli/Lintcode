from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            
            # pruning: rule out repeat nums
            while left + 1 < right and nums[left] == nums[left + 1]:
                left += 1
            while left + 1 < right and nums[right] == nums[right - 1]:
                right -= 1
            
            # return the first element if it is a monotonic increasing array
            # more efficient w/ this part but it works w/o this part
            # if nums[right] > nums[left]:
            #     return nums[left]
            
            # the same as 159
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])
