# https://www.lintcode.com/problem/212/description

class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        if not string:
            return 0

        # 1st time traversal for all spaces
        space = 0
        for s in string:
            if s == ' ':
                space += 1
        
        L = length + 2 * space
        index = L - 1

        # 2nd time traversal to replace all spaces and it goes from back to the front
        for i in range(length - 1, -1, -1):
            if string[i] != ' ':
                string[index] = string[i]
                index -= 1
            else:
                string[index] = '0'
                string[index - 1] = '2'
                string[index - 2] = '%'
                index -= 3
        
        return L
