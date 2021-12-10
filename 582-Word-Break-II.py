class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
    
    # 找到 s 的所有切割方案并 return
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
            
        if len(s) == 0:
            return []
            
        partitions = []
        
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)
                
        if s in wordDict:
            partitions.append(s)
            
        memo[s] = partitions
        return partitions

###
### DFS版本 最终会TLE
###
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        max_length, dict_lower = self.initialize(wordDict)
        res = []
        self.dfs(s, wordDict, [], 0, res, max_length)
        return res
    
    def dfs(self, s, wordDict, chars, index, res, max_length):
        if ''.join(chars) == s:
            res.append(' '.join(chars))
            return

        for i in range(index, len(s)):
            word = s[index:i+1]
            if i + 1 - index > max_length:
                break
            if word not in wordDict:
                continue
            chars.append(word)
            self.dfs(s, wordDict, chars, i + 1, res, max_length)
            chars.pop()
