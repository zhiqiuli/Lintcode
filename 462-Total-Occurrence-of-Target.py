class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        if not A:
            return 0
        left  = self.bisect_left (A, target)
        if left == -1:
            return 0
        right = self.bisect_right(A, target)
        return right - left + 1

    def bisect_left(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] >= target: # 结果肯定在mid左边
                right = mid
            else:
                left  = mid
        if A[left]  == target: return left
        if A[right] == target: return right
        return -1
 
    def bisect_right(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] <= target: # 结果肯定在右边
                left = mid
            else:
                right  = mid
        if A[right] == target: return right # 注意顺序
        if A[left]  == target: return left
        return -1
