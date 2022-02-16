class Solution:
    """
    @param str: a string
    @return: return a string
    """
    # 1. Naive Python way
    #def reverseWords(self, str):
    #    str_list = str.split(' ')
    #    res = ' '.join(str_list[::-1])
    #    return 
    
    # 2. Double reverse way
    def reverseWords(self, str):
        str = self.reverse(str)
        pre = 0
        res = ''
        for i in range(1, len(str)):
            if str[i] == ' ':
                str_ = self.reverse(str[pre:i])
                res += str_ + ' '
                pre  = i + 1
            if i == len(str) - 1:
                str_ = self.reverse(str[pre:])
                res += str_
        return res
    
    def reverse(self, string):
        string = list(string)
        left, right = 0, len(string) - 1
        while left < right:
            string[left], string[right] = string[right], string[left]
            left  += 1
            right -= 1
        return ''.join(string)
