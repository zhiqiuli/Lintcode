# https://www.lintcode.com/problem/1343/?_from=collection&fromId=161

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        i, j = len(A)-1, len(B)-1
        res = []
        while i >= 0 and j >= 0:
            ab = int(A[i]) + int(B[j])
            if ab >= 10:
                res.append(str(ab)[::-1])
            else:
                res.append(str(ab))
            i -= 1
            j -= 1
        while i >= 0:
            res.append(A[i])
            i -= 1
        while j >= 0:
            res.append(B[j])
            j -= 1
        return ''.join(res)[::-1]
