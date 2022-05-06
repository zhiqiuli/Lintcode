from typing import (
    List,
)

from functools import cmp_to_key

class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largest_number(self, nums: List[int]) -> str:
        nums = sorted(nums, key=cmp_to_key(lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1))
        if nums[0] == 0: return '0'
        return ''.join([str(i) for i in nums])
