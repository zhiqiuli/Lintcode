class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        ans = [sys.maxsize] * (amount + 1)
        ans[0] = 0
        for i in coins:
            for j in range(i, amount + 1):
                ans[j] = min(ans[j], ans[j - i] + 1)
        return -1 if ans[-1] == sys.maxsize else ans[-1]
