from typing import (
    List,
)

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trap_rain_water(self, heights: List[int]) -> int:
        # write your code here
        if not heights: return 0
        l, r = 0, len(heights) - 1
        max_l, max_r = heights[l], heights[r]
        res = 0
        while l < r:
            # 是否能积水取决于短板 此处也不需要等号
            if max_r > max_l:
                l += 1
                res += max(0, max_l - heights[l])
                max_l = max(max_l, heights[l])
            else:
                r -= 1
                res += max(0, max_r - heights[r])
                max_r = max(max_r, heights[r])
        return res



class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trap_rain_water(self, heights: List[int]) -> int:
        # write your code here
        if not heights:
            return 0
        res = 0
        for i in range(len(heights)):
            # return 0 if an empty array is given
            left_max = max(heights[:i], default=0)
            rite_max = max(heights[i+1:], default=0)
            res += max(0, min(left_max, rite_max) - heights[i])
        return res



class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trap_rain_water(self, heights: List[int]) -> int:
        
        if not heights:
            return 0

        n = len(heights)
        l = [0] * n
        r = [0] * n
        
        l[0] = heights[0]
        for i in range(1, n):
            l[i] = max(l[i-1], heights[i])
        
        r[n-1] = heights[n-1]
        for i in range(n - 2, -1, -1):
            r[i] = max(r[i+1], heights[i])
        
        res = 0
        for i in range(1, n - 1):
            res += max(0, min(r[i], l[i]) - heights[i])
        
        return res



