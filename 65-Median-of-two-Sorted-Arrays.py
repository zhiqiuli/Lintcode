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
        if len(a) > len(b):
            return self.find_median_sorted_arrays(b, a)
        
        x, y = len(a), len(b)
        
        # binary search in the shorter array
        low = 0
        high = x
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX  = -sys.maxsize if partitionX == 0 else a[partitionX - 1]
            minRightX =  sys.maxsize if partitionX == x else a[partitionX]

            maxLeftY  = -sys.maxsize if partitionY == 0 else b[partitionY - 1]
            minRightY =  sys.maxsize if partitionY == y else b[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY) ) / 2
                else:
                    return  max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
            
            print(maxLeftX, minRightX, maxLeftY, minRightY)
