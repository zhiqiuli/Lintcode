class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        left  = self.binary_left (A, target)
        right = self.binary_right(A, target)
        return [left, right]
    
    def binary_left (self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

    def binary_right (self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            return end
        if A[start] == target:
            return start
        return -1
