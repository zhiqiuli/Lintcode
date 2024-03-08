from typing import (
    List,
)

import sys

class Solution:
    """
    @param a: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number

    核心思路还是同向双指针，枚举右端点，左端点不回头，
    时间复杂度O(n)
    """
    def continuous_subarray_sum(self, a: List[int]) -> List[int]:
        left = 0
        presum = 0
        res = [-1, -1]

        max_sum = -sys.maxsize

        for right in range(len(a)):
            
            # if presum < 0, then reset presum as a[right] & update left
            # otherwise update presum
            if presum < 0:
                presum = a[right]
                left = right
            else:
                presum += a[right]
            
            if presum > max_sum:
                max_sum = presum
                res[0], res[1] = left, right

        return res
