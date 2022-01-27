class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(2, len(s) + 1):
            # dp[i] = dp[i-1] | s[i-1] 对应一个有效字母 + dp[i-2] | s[i-2]s[i-1] 对应两个有效字母
            if 10 <= int(s[i-2] + s[i-1]) <= 26 and s[i-1] != '0':
                dp[i] = dp[i-1] + dp[i-2]
            # s[i-2]s[i-1] 对应两个有效字母并且s[i-1]对应字母无效，则是 10 or 20
            elif int(s[i-2] + s[i-1]) == 10 or int(s[i-2] + s[i-1]) == 20:
                dp[i] = dp[i-2]
            # s[i-1] 对应一个有效字母
            elif s[i-1] != '0':
                dp[i] = dp[i-1]
            # 此时肯定是'x0'或'0x'出现
            else:
                return 0
        return dp[-1]
