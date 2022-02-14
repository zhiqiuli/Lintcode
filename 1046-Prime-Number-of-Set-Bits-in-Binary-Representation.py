import math
class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):

        primes = self.all_primes(int(math.sqrt(R)) + 1)

        results = set()
        n = R
        while n >= L:
            tmp = n
            count = 0
            while tmp:
                count += (tmp & 1)
                tmp >>= 1
            if n not in results and primes[count]:
                results.add(n)
            n -= 1
        return len(results)
    
    def all_primes(self, num):
        res = [True] * (num + 1)
        res[0] = False
        res[1] = False
        for i in range(2, int(math.sqrt(num)) + 1):
            if res[i]:
                j = 2
                while j * i < num + 1:
                    res[j * i] = False
                    j += 1
        return res
