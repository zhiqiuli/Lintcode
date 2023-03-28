class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def drop_eggs(self, n: int) -> int:
        left, right = 1, n # left boundary is only 1 way; right boundary is n ways
        # basically looking for the smallest x such that (1+x)x/2 >= n
        # 1, 2, ..., ..., x0, x1, x2, [x3], [x4], [x5], ... n
        # then [x3] is what we are looking for
        while left + 1 < right:
            mid = (left + right ) // 2
            if (1 + mid) * mid / 2 >= n:
                right = mid
            else:
                left = mid
        if (1 + left) * left / 2 >= n:
            return left
        if (1 + right) * right / 2 >= n:
            return right


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
