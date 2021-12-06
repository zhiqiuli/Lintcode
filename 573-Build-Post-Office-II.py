# https://www.lintcode.com/problem/573/description?_from=collection&fromId=161

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        n, m   = len(grid), len(grid[0])
        dist   = [[sys.maxsize for _ in range(m)] for _ in range(n)]
        counts = [[          0 for _ in range(m)] for _ in range(n)]
        nums   = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, counts)
                    nums += 1
                    
        min_dist = sys.maxsize
        for i in range(n):
            for j in range(m):
                if counts[i][j] == nums and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        
        return min_dist if min_dist != sys.maxsize else -1
    
    # 搜索post office (i,j) 到每个空地的距离
    def bfs(self, grid, i, j, dist, counts):
        queue   = collections.deque([(i, j)])
        visited =               set([(i, j)])
        level   = 0

        while queue:
            for _ in range(len(queue)): # 寻找的是最短距离 所以使用for _ in range(len(queue))
                x, y = queue.popleft()
                if dist[x][y] == sys.maxsize:
                    dist[x][y] = 0
                dist[x][y] += level # dist记录了每个grid点到每个post office的总距离
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x_next, y_next = x + dx, y + dy
                    if self.is_valid(grid, visited, x_next, y_next):
                        counts[x_next][y_next] += 1 # count记录了每个grid到post office的数量
                        queue.append((x_next, y_next))
                        visited.add((x_next, y_next))
            level += 1
                        
    def is_valid(self, grid, visited, i, j):
        n, m   = len(grid), len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        if (i, j) in visited:
            return False
        if grid[i][j] == 1 or grid[i][j] == 2:
            return False
        return True
