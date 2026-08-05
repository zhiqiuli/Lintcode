from typing import (
    List,
)

class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def max_area(self, heights: List[int]) -> int:
        if not heights:
            return 0
        left, right = 0, len(heights) - 1
        area = -sys.maxsize
        while left < right:
            area = max(area, (right - left) * min(heights[left], heights[right]))
            # 无论移动左指针还是右指针，底的长度都是一样的。考虑左边高度高于右边高度，移动右边的指针才可能让结果更大。
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return area
