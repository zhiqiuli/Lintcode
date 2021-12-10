class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        return self.dfs(s, p, 0, 0, {})

    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if s[i:] == '':
            return self.is_empty(p[j:])

        if p[j:] == '':
            return s[i:] == ''

        if j + 1 < len(p) and p[j + 1] == '*':
            matched = self.dfs(s, p, i, j + 2, memo) or \
                      ((s[i] == p[j] or p[j] == '.') and self.dfs(s, p, i + 1, j, memo))
        else:
            matched =  (s[i] == p[j] or p[j] == '.') and self.dfs(s, p, i + 1, j + 1, memo)
        
        memo[(i, j)] = matched
        return memo[(i, j)]
    
    # if s='' and p='a*b*' this will return True as well
    def is_empty(self, pattern):
        if len(pattern) % 2 == 1:
            return False
        
        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != '*':
                return False
        return True
