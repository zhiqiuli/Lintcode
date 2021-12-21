https://www.lintcode.com/problem/654/description
  
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        n1, m1 = len(A), len(A[0])
        n2, m2 = len(B), len(B[0])

        C = [[0] * m2 for _ in range(n1)]

        for i in range(n1):
            for j in range(m2):
                res = 0
                for k in range(n2):
                    if A[i][k] != 0 and B[k][j] != 0:
                        res = res + A[i][k] * B[k][j]
                C[i][j] = res
        
        return C
