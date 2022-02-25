# 纯数学题
# 条件中正整数非常重要
# A后面肯定会放一个/，相当于A是分子，想要分母A/(B C D)最大，那肯定是(B C D)越小越好，条件说明都是正整数，所以B/C/D是最小的，此时结果A/(B/C/D)为最大

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array
    @return: the corresponding expression in string format
    """
    def optimal_division(self, nums: List[int]) -> str:
        # Write your code here
        if len(nums) == 1: return str(nums[0])
        if len(nums) == 2: return str(nums[0]) + '/' + str(nums[1])
        res = str(nums[0]) + '/('
        for i, num in enumerate(nums[1:]):
            if i == 0:
                res += str(num)
            else:
                res += '/' + str(num)
        res += ')'
        return res
