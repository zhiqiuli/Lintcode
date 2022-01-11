class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        if not n: return []
        res = []
        self.dfs(n, k, 0, [], res)
        return res
    
    def dfs(self, n, k, index, path, res):
        if len(path) == k:
            res.append(path[:])
            return
        
        for i in range(index, n):
            path.append(i + 1)
            self.dfs(n, k, i + 1, path, res)
            path.pop()
