https://www.lintcode.com/problem/28/?_from=collection&fromId=161
  
from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left  = self.map2index(0    , 0    , m, n)
        right = self.map2index(m - 1, n - 1, m, n)
        while left + 1 < right:
            mid = (left + right) // 2
            x, y = self.index2map(mid, m, n)
            if matrix[x][y] >= target:
                right = mid
            else:
                left = mid

        x, y = self.index2map(left , m, n)
        if matrix[x][y] == target:
            return True
        x, y = self.index2map(right, m, n)
        if matrix[x][y] == target:
            return True
        return False

    def index2map(self, index, m, n):
        return index // n, index % n
    
    def map2index(self, i, j, m, n):
        return i * n + j
