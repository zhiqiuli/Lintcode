# https://www.lintcode.com/problem/611/description?_from=collection&fromId=161

from collections import deque

DIRECTIONS =[(+ 1, + 2),(+ 1, - 2),(- 1, + 2),(- 1, - 2),(+ 2, + 1),(+ 2, - 1),(- 2, + 1),(- 2, - 1)]

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        n, m = len(grid), len(grid[0])
        queue = deque([(source.x, source.y)])
        distance = {(source.x, source.y) : 0} # distance充当了visited的功能，deque以后马上进入到distance中
        while queue:
            x_cur, y_cur = queue.popleft()
            if (x_cur, y_cur) == (destination.x, destination.y): # 在这里判断是否到达destination 返回不需要+1
                return distance[(x_cur, y_cur)]
            for (dx, dy) in DIRECTIONS:
                x_next, y_next = x_cur + dx, y_cur + dy
                if not self.is_valid(grid, distance, n, m, x_next, y_next):
                    continue
                queue.append((x_next, y_next))
                distance[(x_next, y_next)] = distance[(x_cur, y_cur)] + 1

        return -1
            
    def is_valid(self, grid, distance, n, m, x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if (x, y) in distance:
            return False
        if grid[x][y]:
            return False
        return True
