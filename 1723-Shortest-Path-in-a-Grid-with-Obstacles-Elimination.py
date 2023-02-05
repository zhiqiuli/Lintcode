from typing import (
    List,
)

from collections import deque

class Solution:
    """
    @param grid: a list of list
    @param k: an integer
    @return: Return the minimum number of steps to walk
    """
    def shortest_path(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        # 还剩k个obstacle走到i,j时需要的step
        visited = set([(0, 0, k)])
        q = deque([(0, 0, k)])
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                x, y, rest = q.popleft()
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx, ny = x + dx, y + dy
                    # inside the range
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0 and (nx, ny, rest) not in visited:
                            if nx == m - 1 and ny == n - 1:
                                return step
                            q.append((nx, ny, rest))
                            visited.add((nx, ny, rest))
                        # 此处需要判断是否还剩余rest
                        elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                            q.append((nx, ny, rest - 1))
                            visited.add((nx, ny, rest - 1))
                        else:
                            pass
        return -1