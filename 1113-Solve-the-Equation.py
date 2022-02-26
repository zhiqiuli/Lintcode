class Solution:
    """
    @param equation: a string
    @return: return a string
    """
    def solve_equation(self, equation: str) -> str:
        left, right = equation.split('=')
        cnt_x_l, sum_l = self.helper(left)
        cnt_x_r, sum_r = self.helper(right)
        if cnt_x_l == cnt_x_r:
            if sum_l != sum_r:
                return 'No solution'
            else:
                return 'Infinite solutions'
        if sum_l == sum_r:
            return 'x=0'
        if cnt_x_l > cnt_x_r:
            return 'x='+str(int((sum_r - sum_l)/(cnt_x_l - cnt_x_r)))
        return 'x='+str(int((sum_l - sum_r)/(cnt_x_r - cnt_x_l)))

    def helper(self, string):
        cnt_x = sum_ = 0 # x系数和常数项
        sign = 1
        num = 0
        for char in string:
            # 读到数字
            if char.isdigit():
                # 这一步很关键 累计x前的系数
                num = num * 10 + int(char)
            # 读到x，代表前一项已经读完了
            elif char == 'x':
                if num:
                    cnt_x += sign * num
                else:
                    cnt_x += sign
                num = 0
            # 读到sign，代表前一项已经读完了
            else:
                sum_ += sign * num
                num  = 0
                sign = 1 if char == '+' else -1
        sum_ += sign * num
        return cnt_x, sum_
