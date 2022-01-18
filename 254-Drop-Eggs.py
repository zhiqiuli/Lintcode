class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        # write your code here
        import math
        x = int(math.sqrt(n * 2)) # 相当于取了一个x的下届
        while x * (x + 1) / 2 < n:
            x += 1
        return x
