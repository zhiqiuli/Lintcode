from typing import (
    List,
)

class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        nums = sorted(nums) # O(N LOG(N))
        res = 0
        for k in range(2, len(nums)):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    res += (j - i)
                    i += 1
                else:
                    j -= 1
        return res
