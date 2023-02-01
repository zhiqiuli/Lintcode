# 没什么技巧，纯是一个数学题
class Solution:
    """
    @param n: the given number
    @return:  return true if it has exactly three distinct factors, otherwise false
    """
    def is_three_disct_factors(self, n: int) -> bool:
        # corner case
        if n == 1:
            return False
        # if n is not a squared number, then it can't be
        if int(math.sqrt(n)) ** 2 != n:
            return False
        # check sqrt(n) is a prime number
        k = int(math.sqrt(n))
        for i in range(2, int(math.sqrt(k)) + 1):
            if k % i == 0:
                return False
        return True
