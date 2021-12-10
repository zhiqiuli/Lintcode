class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        res_1, res_2, res_3 = 1, 1, 2
        for _ in range(3, n + 1):
            res = res_1 + res_2 + res_3
            res_1, res_2, res_3 = res_2, res_3, res
        return res
