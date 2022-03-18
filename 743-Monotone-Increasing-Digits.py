class Solution:
    """
    @param num: a non-negative integer N
    @return: the largest number that is less than or equal to N with monotone increasing digits.
    """
    def monotone_digits(self, num: int) -> int:
        digits = [0] * 10
        cnt = 0
        # 87 -> 7, 8
        while num != 0:
            digits[cnt] = num % 10
            cnt += 1
            num //= 10

        for i in range(1, cnt):
            # 7, 8
            if digits[i] > digits[i-1]:
                # as 7 < 8 -> 8 - 1 = 7 -> 7, 7
                digits[i] -= 1
                # 7, 7 -> 9, 7
                for k in range(i):
                    digits[k] = 9
        
        ans = 0
        for i in range(cnt-1, -1, -1):
            ans = 10 * ans + digits[i]

        return ans
