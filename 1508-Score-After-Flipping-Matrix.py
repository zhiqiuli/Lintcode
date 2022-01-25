class Solution:
    """
    @param A: a matrix
    @return: the score
    """
    def matrixScore(self, A):
        M, N = len(A), len(A[0])
        # 为使总和最大则尽可能使权重大的格子填“1”。最左边一列权重最大，所以总可以通过
        # 行翻转使左边第一列全都置“1”，后面就不能再使用行翻转了，以免破环当前的结构，
        res_sum = M * (1 << N - 1)
        for j in range(1, N):
            # 此row第一个是1 则不需要反转 考虑所有1
            # 此row第一个是0 则需要反转 所以考虑0
            cur_sum  = sum(A[i][j] == A[i][0] for i in range(M))
            cur_sum  = max(cur_sum, M - cur_sum) * (1 << N - 1 - j)
            res_sum += cur_sum
        return res_sum
