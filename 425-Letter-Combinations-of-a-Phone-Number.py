num2letter = {'2' : 'abc',
              '3' : 'def',
              '4' : 'ghi',
              '5' : 'jkl',
              '6' : 'mno',
              '7' : 'pqrs',
              '8' : 'tuv',
              '9' : 'wxyz'}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, res, [])
        return res
    
    def dfs(self, digits, index, res, chars):
        # 递归的出口
        if index == len(digits):
            res.append(''.join(chars))
            return

        for letter in num2letter[digits[index]]:
            chars.append(letter) # 递归append
            self.dfs(digits, index + 1, res, chars)
            chars.pop() # 递归pop
