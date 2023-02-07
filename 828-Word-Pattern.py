class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def word_pattern(self, pattern: str, s: str) -> bool:
        # write your code here
        words = s.split(' ') # dog,cat,cat,dog
        used = set()
        mapping = {}

        # 长度不一样，直接返回False
        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            
            # 如果已存在key，则mapping[key]等于words[i]
            if char in mapping:
                if mapping[char] != words[i]:
                    return False
            
            if char not in mapping:
                # 如果需要添加新的words，words不能存在used之中
                if words[i] in used:
                    return False
                mapping[char] = words[i]
                used.add(words[i])
        
        return True
