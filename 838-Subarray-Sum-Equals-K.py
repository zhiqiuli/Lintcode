from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarray_sum_equals_k(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_ = 0
        presum_count = {0:1} # nums=[1] & k=1
        res = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            res += presum_count.get(sum_ - k, 0)
            presum_count[sum_] = presum_count.get(sum_, 0) + 1
        return res
