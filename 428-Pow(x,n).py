class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        
        if n < 0:
            n, sign = -n, -1
        else:
            n, sign =  n,  1
        
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = ans * x
            x = x * x
            n = n // 2
        
        if sign == 1:
            return ans
        else:
            return 1.0 / ans
