class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    def is_perfect_square(self, num: int) -> bool:
        start, end = 1, num // 2
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid
            else:
                start = mid
        if start * start == num or end * end == num:
            return True
        return False
