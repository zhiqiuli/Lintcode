class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        return self.dfs(s, p, 0, 0, {})

    # 记忆搜索需要返回某个值
    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # Case 1 - if source is empty
        if s[i:] == '':
            # p is empty or every character in p should be "*"
            if p[j:] == '':
                return True
            return len(set(p[j:])) == 1 and p[j] == '*' 

        # Case 2 - if pattern is empty
        if p[j:] == '':
            return s[i:] == ''

        if p[j] != '*':
            matched = (s[i] == p[j] or p[j] == '?') and self.dfs(s, p, i + 1, j + 1, memo)
        else:
            matched = self.dfs(s, p, i, j + 1, memo) or self.dfs(s, p, i + 1, j, memo)

        memo[(i, j)] = matched
        return matched
