class Solution:
    """
    @param n: an unsigned integer
    @return: the number of ’1' bits
    """
    def hammingWeight(self, n):
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        return count
