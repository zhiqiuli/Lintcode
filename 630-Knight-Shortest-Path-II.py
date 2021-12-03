# https://www.lintcode.com/problem/630/description?_from=collection&fromId=161

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        queue    = collections.deque([(0, 0)])
        distance = 0
        
        while queue:
            distance += 1
            for _ in range(len(queue)): # 搜索的是最短路径
                x, y = queue.popleft()
                for (dx, dy) in [(1, 2), (-1, 2), (2, 1), (-2, 1)]:
                    x_next, y_next = x + dx, y + dy
                    if self.is_valid(x_next, y_next, grid, visited):
                        queue.append((x_next, y_next))
                        visited[x_next][y_next] = True
                        # move到下一个时进行判断是否能返回,需要放在is_valid里面,有可能grid[m-1][n-1]==1
                        if (x_next, y_next) == (m - 1, n - 1):
                            return distance
        return -1
            
    def is_valid(self, x, y, grid, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if visited[x][y] or grid[x][y]:
            return False
        return True
