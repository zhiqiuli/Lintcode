KEY:
  1. 使用stack保存数据
  2. sign保存的是前一个符号 默认起始+
  
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+' # sign保存的是前一个sign，默认开始为+
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)
            # 遇到+-*/时，或者i等于len(s)-1时，进行统计是否进
            if c in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = c
        return sum(stack)
