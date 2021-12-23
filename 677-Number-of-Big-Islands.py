class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """
    def numsofIsland(self, grid, k):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count   = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    if self.bfs(grid, visited, i, j) >= k:
                        count += 1
        return count
    
    def bfs(self, grid, visited, x, y):
        queue    = collections.deque([(x, y)])
        landsize = 1 
        while queue:
            x_now, y_now = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x_next, y_next = x_now + dx, y_now + dy
                if self.is_valid(x_next, y_next, grid, visited):
                    queue.append((x_next, y_next))
                    visited[x_next][y_next] = True
                    landsize += 1
        return landsize
    
    def is_valid(self, x, y, grid, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if visited[x][y] or grid[x][y] == 0:
            return False
        return True
