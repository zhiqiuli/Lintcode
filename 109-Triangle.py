class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0

        #   状态转移方程 f[i][j] = g[i][j] + min(f[i-1][j], f[i-1][j-1])
        prev_res = [triangle[0][0]]
        for i in range(1, len(triangle)):
            # print(prev_res)
            res = [0] * (i + 1)
            for j in range(i + 1):
                if j == 0:
                    res[j] = triangle[i][j] + prev_res[j]
                elif j == i:
                    res[j] = triangle[i][j] + prev_res[i - 1]
                else:
                    res[j] = triangle[i][j] + min(prev_res[j], prev_res[j-1])
            prev_res = res[:]
        return min(prev_res)
