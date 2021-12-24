class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        return self.bfs(maze, start, destination)
    
    def bfs(self, maze, start, destination):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = collections.deque([start])
        while queue:
            
            x, y = queue.popleft()

            if [x, y] == destination:
                return True
            for dx, dy in directions:
                row = x + dx
                col = y + dy
                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                    row += dx
                    col += dy
                row -= dx
                col -= dy
                if maze[row][col] == 0:
                    queue.append([row, col])
                    maze[row][col] = 2 # 当maze[row][col]==2时 期充当了visited的作用 记住queue.append总是和visited.add在一起
        return False
