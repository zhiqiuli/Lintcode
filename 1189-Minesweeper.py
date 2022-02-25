from typing import (
    List,
)

directions = [(-1,-1), (-1,0), (-1, 1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

class Solution:
    """
    @param board: a board
    @param click: the position
    @return: the new board
    """
    def update_board(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        
        # 第一次点击是M的话 游戏结束
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        # 第一次点击不是M 游戏可以继续 采用BFS
        queue = collections.deque([(click[0], click[1])])
        while queue:
            x, y = queue.popleft()
            # 点击的是E 有两种情况
            # 情况1 周围没有雷 a.显示为B b.将周围所有点放入queue
            # 情况2 周围有雷 a.显示为数字 b.周围的点都不放入queue
            if board[x][y] == 'E':
                num_mines, positions = self.count(board, x, y, m, n)
                if num_mines == 0:
                    board[x][y] = 'B'
                    queue.extend(positions)
                else:
                    board[x][y] = str(num_mines)
        return board
    
    def is_valid(self, board, x, y, m, n):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        return True
    
    def count(self, board, x, y, m, n):
        count = 0
        positions = []
        for dx, dy in directions:
            x_next, y_next = x + dx, y + dy
            if self.is_valid(board, x_next, y_next, m, n):
                positions.append((x_next, y_next))
                if board[x_next][y_next] == 'M':
                    count += 1
        return count, positions
