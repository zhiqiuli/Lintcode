class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, string):
        res = []
        self.dfs(n, string, [], res)
        sum = 0
        for p in res[0]:
            sum += int(p)
        return n * (n+1) // 2 - sum
    
    def dfs(self, n, string, path, res):
        if not string:
            res.append(path[:])
            return
        for i in range(2):
            num = string[:i + 1]
            if num in path or int(num) > n or num[0] == '0':
                continue
            path.append(num)
            self.dfs(n, string[i + 1:], path, res)
            path.pop()
