from typing import (
    List,
)

class Solution:
    """
    @param a: The array A.
    @return: The array of the squares.
    """
    def square_array(self, a: List[int]) -> List[int]:
        start, end = 0, len(a) - 1
        res = []
        while start <= end:
            if abs(a[end]) > abs(a[start]):
                res.append(a[end] * a[end])
                end -= 1
            else:
                res.append(a[start] * a[start])
                start += 1
        return res[::-1]
