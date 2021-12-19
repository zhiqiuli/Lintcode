class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x <= 0:
            return 0
        
        x_0 = x
        x_1 = x_0 + (x - x_0 ** 2) / (2 * x_0)
        err = abs(x_0 - x_1)

        while err > 0.5:
            x_1 = x_0 + (x - x_0 ** 2) / (2 * x_0)
            err = abs(x_0 - x_1)
            x_0 = x_1

        return int(x_1)
