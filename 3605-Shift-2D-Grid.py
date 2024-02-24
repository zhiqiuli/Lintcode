from typing import (
    List,
)

class Solution:
    """
    @param grid: m*n matrix
    @param k: Number of shifts
    @return: m*n matrix after shift
    """
    def shift_grid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # construct an array
        m, n = len(grid), len(grid[0])
        theList = []
        for i in range(m):
            for j in range(n):
                theList.append(grid[i][j])
        
        # permutate the array
        theList = theList[-k:] + theList[:-k]
        
        # replace the elements w/ new order
        l = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = theList[l]
                l += 1
        
        return grid