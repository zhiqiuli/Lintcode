'''
思路：
给的n，每次除一个2～math.sqrt(n) 之间能整除的数字。
每次递归进来之后，只要path不是空，都是能被整除的解，所以直接加到result。

math.sqrt(n) 很巧妙，会保证8只会被分解成2，2，2 和 2，4，而不会被分解成 4，2。
'''
import math

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        res = []
        self.dfs(n, 2, [], res)
        return res
    
    def dfs(self, n, index, path, res):
        if len(path) != 0:
            res.append(path[:] + [n]) # 不同于别的dfs 此处不需要return 每一步都叠加factor
        for factor in range(index, int(math.sqrt(n)) + 1):
            if n % factor == 0:
                path.append(factor)
                self.dfs(n // factor, factor, path, res)
                path.pop()
