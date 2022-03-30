class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    def kth_prime(self, n: int) -> int:
        isprime = [True] * (n + 1)
        for i in range(2, n + 1):
            k = 2
            while i * k < n + 1:
                isprime[i * k] = False
                k += 1
        # 跳过前两个元素[0,1]，这两个并不是primes
        return isprime[2:].count(True)
