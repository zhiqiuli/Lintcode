# https://www.lintcode.com/problem/683/description?_from=collection&fromId=161
class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        max_length, dict_lower = self.initialize(dict)
        return self.dfs(s.lower(), dict_lower, max_length, {}, 0) # 需要传入lower的s 坑爹
    
    def dfs(self, s, dict_lower, max_length, memo, index):
        
        # 递归的退出条件
        if len(s) == index:
            return 1

        # 如果结果已存在 无需再计算 直接返回答案
        if index in memo:
            return memo[index]
        
        memo[index] = 0
        for i in range(index, len(s)):
            if i+1-index > max_length: # 超过最大长度 无需继续
                break
            word = s[index:i+1] # 所以substring的长度是i+1-index
            if word not in dict_lower:
                continue
            memo[index] += self.dfs(s, dict_lower, max_length, memo, i + 1)

        return memo[index]

    # initialize dict -> max length & dict in lower case
    def initialize(self, dict):
        dict_lower = set()
        max_len    = -sys.maxsize
        for d in dict:
            dict_lower.add(d.lower())
            max_len = max(max_len, len(d))
        return max_len, dict_lower
