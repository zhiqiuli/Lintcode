# https://www.lintcode.com/problem/598/?_from=collection&fromId=161
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        n, m = len(grid), len(grid[0])

        # 找到所有的zombie
        queue = collections.deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j))

        time = 0
        while queue:
            if self.check_answer(grid): # grid 记录了当前情况
                return time
            time += 1
            for _ in range(len(queue)): # 最短时间bfs
                (x, y) = queue.popleft()
                for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x_next, y_next = x + dx, y + dy
                    if not self.is_valid(x_next, y_next, grid):
                        continue
                    queue.append((x_next, y_next))
                    grid[x_next][y_next] = 1
        return -1
    
    # check是否下一步是valid
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if grid[x][y] != 0:
            return False
        return True
    
    # check是否全部是zombie
    def check_answer(self, grid):
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    return False
        return True
