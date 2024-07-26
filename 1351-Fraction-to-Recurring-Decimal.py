class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # 包含了numerator==0
        if numerator % denominator == 0:
            return str(numerator // denominator)

        sign = '-' if numerator * denominator < 0 else ''
        num, den = abs(numerator), abs(denominator)

        # n是整数部分
        n, rem = divmod(num, den)
        res = sign + str(n) + '.'
        
        #rem_to_pos保存余数所在位置
        num_to_pos = {}

        # 余数为零（整除），出现了重复的余数（意味着循环出现）
        while rem and rem not in num_to_pos: 
            num_to_pos[rem] = len(res)
            n, rem = divmod(10 * rem, den)
            res += str(n)
        
        if rem in num_to_pos: # 这里的判断也可以用 if rem:
            #如果rem重复，在对应的位置 插入 '('
            index = num_to_pos[rem]
            res = res[:index] + '(' + res[index:] + ')'
        
        return res