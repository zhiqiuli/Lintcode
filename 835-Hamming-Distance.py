class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        diff_count = 0
        for i in range(31, -1, -1):
            diff_count += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        return diff_count
