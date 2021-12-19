https://www.lintcode.com/problem/1870/?_from=collection&fromId=161

class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def stringCount(self, str):
        total = 0
        sub   = 0
        for s in str:
            if s == '0':
                sub += 1
            else:
                total += sub * (sub + 1) // 2 # 全部的substrings即是全排列
                sub = 0
        total += sub * (sub + 1) // 2
        return total
