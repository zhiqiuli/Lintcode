class Solution:
    """
    @param targetMap: 
    @return: nothing
    """
    def shortestPath(self, targetMap):
        queue = collections.deque([(0, 0)])
        visited = set([(0, 0)])
        dist = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if targetMap[x][y] == 2:
                    return dist
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    x_new, y_new = x + dx, y + dy
                    if self.is_valid(x_new, y_new, targetMap, visited):
                        visited.add((x_new, y_new))
                        queue.append((x_new, y_new))
            dist += 1
        return -1
        
    def is_valid(self, x, y, grid, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        if grid[x][y] == 1:
            return False
        return True
