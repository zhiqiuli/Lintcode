class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        if not words:
            return []
        
        res = []
        size = len(words[0])
        prefix = dict()
        # create prefix hash mapp
        # -----------------------------
        # key: ''   l    le   lea  lead
        # -----------------------------
        # val: lead lead lead lead lead
        #      lady lady
        #      area
        # -----------------------------
        for w in words:
            for i in range(len(w) + 1):
                set_of_word = prefix.get(w[0:i], set())
                set_of_word.add(w)
                prefix[w[0:i]] = set_of_word
        self.dfs(res, [], size, prefix)
        return res
    
    def dfs(self, res, path, size, prefix):
        if len(path) == size:
            res.append(list(path))
            return 
        
        current_row = len(path)
        head = ''
        for word in path:
            head += word[current_row]
        # pruning
        # 当前若是ball
        # 只判断a是否存在prefix中并进行到下一层
        if head not in prefix:
            return
        for w in prefix[head]:
            path.append(w)
            self.dfs(res, path, size, prefix)
            path.pop()
