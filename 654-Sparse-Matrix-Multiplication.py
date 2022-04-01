from typing import (
    List,
)

class Solution:
    """
    @param a: a sparse matrix
    @param b: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        
        n = len(a)
        m = len(a[0])
        k = len(b[0])

        row_vector = [
            [(j, a[i][j]) for j in range(m) if a[i][j] != 0]
            for i in range(n)
        ]

        vol_vector = [
            [(i, b[i][j]) for i in range(m) if b[i][j] != 0]
            for j in range(k)
        ]

        C = [[0] * k for _ in range(n)]
        for i in range(n):
            for j in range(k):
                C[i][j] = self.multiply_vec(row_vector[i], vol_vector[j])
        return C

    def multiply_vec(self, v1, v2):
        i, j, sum = 0, 0, 0
        while i < len(v1) and j < len(v2):
            index1, val1 = v1[i]
            index2, val2 = v2[j]
            if index1 > index2:
                j += 1
            elif index1 < index2:
                i += 1
            else:
                sum += val1 * val2
                i += 1
                j += 1
        return sum

'''
'''
'''
      
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
