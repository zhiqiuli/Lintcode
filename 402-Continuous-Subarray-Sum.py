from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuous_subarray_sum(self, a: List[int]) -> List[int]:
        runningSum = maxSum = a[0]
        maxLo = maxHi = lo = hi = 0
        # enumerate 可以选择从某一个index开始，譬如说这里就是start=1
        for hi, num in enumerate(a[1:], start=1):
            # 如果running < 0，reset runningSum
            if runningSum < 0:
                runningSum = num
                lo = hi
            else:
                runningSum += num
            
            if runningSum > maxSum:
                maxLo, maxHi, maxSum = lo, hi, runningSum
        
        return maxLo, maxHi