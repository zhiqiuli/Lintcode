'''
dp[i][j]代表s1前i位（包含）与s2前j位（包含）匹配所需要的最小代价。

dp[i][j] = min {
    dp[i - 1][j - 1] when s1[i - 1] matches s2[j - 1], <-- no cost when last char matching
    dp[i - i][j] + s1[i - 1], <-- remove s1's last char
    dp[i][j - 1] + s2[j - 1] <-- remove s2's last char
}

dp[0][:] 当s1是空串的时候，费用就是删去s2的前j个（包含）字符
dp[:][0] 当s2是空串的时候，费用就是删去s1的前i个（包含）字符
'''
class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: the lowest ASCII sum of deleted characters to make two strings equal
    """
    def minimumDeleteSum(self, s1, s2):
        n1, n2 = len(s1), len(s2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), \
                                   dp[i][j - 1] + ord(s2[j - 1]))
        return dp[-1][-1]
