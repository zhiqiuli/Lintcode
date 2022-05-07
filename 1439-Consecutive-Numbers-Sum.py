class Solution:
    """
    @param n: an integer
    @return: how many ways can we write it as a sum of consecutive positive integers
    """
    def consecutive_numbers_sum(self, n: int) -> int:
        # 假设序列是 x + x+1 + x+2 + ... + x+m-1 = (x+m-1 + x) * m / 2 = N
        # (2x + m - 1) * m / 2 = N
        # 基本思路扫描可行的m和x，使得以上方程满足
        # 2x + m - 1 = 2N / m => 2x = 2N / m - m + 1 => x = N/m - m/2 + 1/2 = (2*N - m^2 + m)/(2*m)
        res = 0
        m = 1
        # while 2*n - m*m + m > 0: # 最保守的做法，确保分子一定大于0
        while m*m < 2*n:
            if (2*n - m*m + m) % (2*m) == 0:
                res += 1
            m += 1
        return res
