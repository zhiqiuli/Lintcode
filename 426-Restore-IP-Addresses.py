class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        if not s:
            return []
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(self, s, startInd, path, res): # 不改变string的写法  
        if len(path) == 4 and startInd == len(s):
            res.append('.'.join(path[:]))
            return

        for i in range(startInd, startInd + 3):
            if i >= len(s):
                return
            substring = s[startInd : i + 1]
            num = int(substring)
            if num < 0 or num > 255 or len(substring) != len(str(num)):
                continue
            path.append(substring)
            self.dfs(s, i + 1, path, res)
            path.pop()
