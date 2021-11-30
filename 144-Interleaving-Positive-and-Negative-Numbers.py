# https://www.lintcode.com/problem/144/?_from=collection&fromId=161

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        pos, neg = 0, 0
        for i in A:
            if i > 0:
                pos += 1
            else:
                neg += 1
        
        A = self.partition (A, pos >  neg)
        A = self.interleave(A, pos == neg)
        return A
    
    def partition(self, A, start_pos):
        flag = 1 if start_pos else -1
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] * flag  > 0:
                left += 1
            while left <= right and A[right] * flag < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left  += 1
                right -= 1
        return A
    
    def interleave(self, A, has_same_len):
        left, right = 1, len(A) - 1
        if has_same_len:
            right = len(A) - 2

        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2
        
        return A
