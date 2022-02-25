from typing import (
    List,
)

# 其实就是个公式
# F[1] - F[0] = sum - n * B[n-1]
# F[2] - F[1] = sum - n * B[n-2]

class Solution:
    """
    @param a: an array
    @return: the maximum value of F(0), F(1), ..., F(n-1)
    """
    def max_rotate_function(self, a: List[int]) -> int:
        s = sum(a)
        curr = sum([i * j for i, j in enumerate(a)])
        maxVal = curr
        n = len(a)
        for i in range(n - 1):
            curr = curr + s - n * a[n-1-i]
            maxVal = max(maxVal, curr)
        return maxVal
