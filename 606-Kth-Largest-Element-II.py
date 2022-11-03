from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kth_largest_element2(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)

    def quick_select(self, nums, start, end, k):
        if start >= end:
            return nums[k]
        left, right = start, end
        mid = (left + right) // 2
        target = nums[mid]
        while left <= right:
            while left <= right and nums[left] < target:
                left += 1
            while left <= right and nums[right] > target:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k <= right:
            return self.quick_select(nums, start, right, k)
        if k >= left:
            return self.quick_select(nums, left, end, k)
        return nums[k]