class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, string):
        return self.dfs(pattern, string, {}, set())
    
    def dfs(self, pattern, string, mapping, used):
        if not pattern:
            return not string

        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not string.startswith(word):
                return False
            return self.dfs(pattern[1:], string[len(word):], mapping, used)

        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:
                continue
            
            used.add(word)
            mapping[char] = word
            if self.dfs(pattern[1:], string[i + 1:], mapping, used):
                return True
            used.remove(word)
            del mapping[char]
        
        return False
