# https://www.lintcode.com/problem/459/description
# very similar to the First Position problem
# add 

class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        if not A:
            return -1

        start, end = 0, len(A) - 1

        # 1
        while start + 1 < end:
            
            # 2
            mid = start + int((end - start) / 2)

            if target >= A[mid]:
                start = mid
            else:
                end = mid
        
        # 4
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        
        # find the closest one
        if target - A[start] >= A[end] - target:
            return end
        else:
            return start
        
        return -1
        
