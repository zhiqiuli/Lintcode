class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                k -= 1
                i -= 1
            else:
                A[k] = B[j]
                k -= 1
                j -= 1
        # i=0时排序已经完成，只需要考虑j>=0时的情况，极端情况考虑如下
        # A []
        # B [2,3,4]
        while j >= 0:
            A[k] = B[j]
            k -= 1
            j -= 1
        return
