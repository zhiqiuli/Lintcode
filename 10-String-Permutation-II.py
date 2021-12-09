#https://www.lintcode.com/problem/10/description?_from=collection&fromId=161

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        chars = sorted(list(str))
        res = []
        self.dfs(chars, 0, [], res, [False] * len(str))
        return res

    def dfs(self, chars, index, s, res, visited):
        if len(chars) == index:
            res.append(''.join(s))
            return
        
        for i in range(len(chars)):
            # 同一个位置上的字符用过不能在用
            if visited[i]:
                continue
            # 去重：不同位置的同样的字符，必须按照顺序用。
            # a' a" b
            # => a' a" b => √
            # => a" a' b => x
            # 不能跳过一个a选下一个a
            if i > 0 and chars[i] == chars[i - 1] and not visited[i - 1]:
                continue

            s.append(chars[i])
            visited[i] = True
            self.dfs(chars, index + 1, s, res, visited)
            s.pop()
            visited[i] = False
