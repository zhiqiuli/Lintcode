# https://www.lintcode.com/problem/132/description?_from=collection&fromId=161
###
### 使用dfs的版本
###
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
        # 如果当前结果不存在prefix_set中，之后肯定也不会，prune
        if word not in prefix_set:
            return
        
        # Key
        # 这个地方不需要退出
        # 譬如说words中有[se,see]，找到se之后可以继续寻找see
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

    
###
### 使用 Trie + dfs的版本
###
class TrieNode:
    def __init__(self):
        self.p = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.p:
                node.p[c] = TrieNode()
            node = node.p[c]
        node.is_word = True
    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.p:
                return False
            node = node.p[c]
        return node.is_word
    def findPrefix(self, word):
        node = self.root
        for c in word:
            if c not in node.p:
                return False
            node = node.p[c]
        return True

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        words = set(words)
        trie = Trie()
        for word in words:
            trie.insert(word)

        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, board[i][j], words, trie, set([(i, j)]), res)
        return list(res)

    def dfs(self, board, x, y, word, word_set, trie, visited, res):
        # 如果当前结果不存在prefix_set中，之后肯定也不会，prune
        if not trie.findPrefix(word):
            return
        
        # Key
        # 这个地方不需要退出
        # 譬如说words中有[se,see]，找到se之后可以继续寻找see
        if trie.find(word):
            res.add(word)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_x, n_y = x + dx, y + dy
            if not self.is_valid(board, visited, n_x, n_y):
                continue
            # dfs模版 word+board[n_x][n_y]这么写还可以节省一个var的input arg
            visited.add((n_x, n_y))
            self.dfs(board, n_x, n_y, word + board[n_x][n_y], word_set, trie, visited, res)
            visited.remove((n_x, n_y))
    
    def is_valid(self, board, visited, x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        if (x, y) in visited:
            return False 
        return True
