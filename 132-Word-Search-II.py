# https://www.lintcode.com/problem/132/description?_from=collection&fromId=161
# 使用dfs的版本
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if len(board) == 0 or len(board[0]) == 0:
            return []

        word_set = set(words) # dict去重复
        prefix_set = set() # 保存word_set里面所有的元
        for word in word_set:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.dfs(board, i, j, board[i][j], word_set, prefix_set, set([(i, j)]), res)

        return list(res)

    def dfs(self, board, x, y, word, word_set, prefix_set, visited, res):
        # 如果当前结果不存在prefix_set中 之后肯定也不会 应该是prune
        if word not in prefix_set:
            return
        # 递归出口
        if word in word_set:
            res.add(word)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_x, n_y = x + dx, y + dy
            if not self.is_valid(board, visited, n_x, n_y):
                continue
            # dfs模版 word+board[n_x][n_y]这么写还可以节省一个var的input arg
            visited.add((n_x, n_y))
            self.dfs(board, n_x, n_y, word + board[n_x][n_y], word_set, prefix_set, visited, res)
            visited.remove((n_x, n_y))
    
    def is_valid(self, board, visited, x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        if (x, y) in visited:
            return False 
        return True
