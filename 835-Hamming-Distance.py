class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        ans = 0
        for i in range(31, -1, -1):
            a = (x >> i) & 1 # 取出bit 0或1
            b = (y >> i) & 1
            if a != b: ans += 1
        return ans
