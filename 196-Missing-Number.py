from typing import (
    List,
)

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def find_missing(self, nums: List[int]) -> int:
        # [0,1,3,4] => [0,1,3,4,4]
        nums.append(len(nums))
        # [0,1,3,4] => [-0,-1,3,-4,-4]
        for num in nums:
            nums[abs(num)] = -nums[abs(num)]
        # [-0,-1,3,-4,-4] => return the first non-negative index
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        return len(nums) - 1
