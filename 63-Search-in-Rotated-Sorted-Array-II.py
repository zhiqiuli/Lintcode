# 跟62很相似，唯一的区别就在于remove掉开头和结尾相同的元素

from typing import (
    List,
)

class Solution:
    """
    @param a: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, nums: List[int], target: int) -> bool:
        # write your code here
        if not nums:
            return False
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            
            # remove首位相同的元素
            while nums[start] == nums[start + 1] and start + 1 < end:
                start += 1
            while nums[end]   == nums[end - 1] and start + 1 < end:
                end -= 1
            
            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            if nums[mid] <= nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid

        if nums[start] == target or nums[end] == target:
            return True

        return False
