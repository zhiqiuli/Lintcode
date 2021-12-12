class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        n, m    = len(board), len(board[0])
        prefix  = set([word[:i + 1] for i in range(len(word))])
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                visited[i][j] = True
                if self.dfs(i, j, board, word, [board[i][j]], visited, prefix):
                    return True
                visited[i][j] = False
        return False
    


    def dfs(self, x, y, board, word, path, visited, prefix):

        n, m = len(board), len(board[0])

        if ''.join(path) not in prefix:
            return False

        if len(path) == len(word):
            return ''.join(path) == word
        
        Result = False

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            n_x, n_y = x + dx, y + dy
            if not self.is_valid(n, m, n_x, n_y) or visited[n_x][n_y]:
                continue
            visited[n_x][n_y] = True
            path.append(board[n_x][n_y])
            Result = Result or self.dfs(n_x, n_y, board, word, path, visited, prefix)
            visited[n_x][n_y] = False
            path.pop()
        
        return Result
    
    def is_valid(self, n, m, x, y):
        if 0 <= x < n and 0 <= y < m:
            return True
        return False
