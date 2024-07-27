from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param b: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def find_median_sorted_arrays(self, a: List[int], b: List[int]) -> float:
        # 总是在短的数组上进行搜索
        if len(a) > len(b):
            return self.find_median_sorted_arrays(b, a)
        
        x, y = len(a), len(b)
        
        low, high = 0, x

        while low <= high:

            # 在X上面进行partition
            partitionX = (low + high) // 2
            
            # Y上的partition取决于如下关系
            partitionY = (x + y + 1) // 2 - partitionX

            # if partitionX is 0 it means nothing on left side. Use -INF for maxLeftX
            # if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
            maxLeftX  = -sys.maxsize if partitionX == 0 else a[partitionX - 1]
            minRightX =  sys.maxsize if partitionX == x else a[partitionX]

            maxLeftY  = -sys.maxsize if partitionY == 0 else b[partitionY - 1]
            minRightY =  sys.maxsize if partitionY == y else b[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # We have partitioned array at correct place
                # Now get max of left elements and min of right elements to get the median in case of even length combined array size
                # or get max of left for odd length combined array size.
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY) ) / 2
                else:
                    return  max(maxLeftX, maxLeftY)

            # we are too far on right side for partitionX. Go on left side.
            # For example:
            #       a: 1, 3, 10 | 11, 12
            #       b: 2, 4, 6  | 8
            # maxLeftX(10) > minRightY(8), go to the left side
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
