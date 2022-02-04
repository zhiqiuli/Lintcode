'''
基本款的BFS， 加上找到xmin， ymin， 然后把所有坐标减去这个， 然后serialize成str， 放入set比较
'''
class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        visited = set()
        islands = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) in visited:
                    continue
                if grid[x][y] == 0:
                    continue
                visited.add((x, y))
                island = self.bfs(grid, x, y, visited)
                islands.add(self.island_to_str(island))
        return len(islands)
    
    def bfs(self, grid, x, y, visited):
        res = []
        queue = collections.deque([(x, y)])
        while queue:
            node = queue.popleft()
            res.append(node)
            for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                x_new, y_new = node[0] + dx, node[1] + dy
                if self.is_valid(x_new, y_new, visited, grid):
                    visited.add((x_new, y_new))
                    queue.append((x_new, y_new))
        return res
    
    def is_valid(self, x, y, visited, grid):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        if grid[x][y] == 0:
            return False
        return True
    
    def island_to_str(self, island):        
        x_min  = sorted(island, key=lambda x: x[0])[0][0] # find min-x
        y_min  = sorted(island, key=lambda x: x[1])[0][1] # find min-y
        island = sorted([(x - x_min, y - y_min) for (x, y) in island])
        return '#'.join([str(x) + ',' + str(y) for (x, y) in island])
