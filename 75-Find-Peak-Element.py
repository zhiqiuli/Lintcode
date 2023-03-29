binary search寻找peak element，因为初始数组的开头是升序，结尾是降序，所以一定存在peak，每一次搜索如果中间点mid仍旧是处于升序段，那后半段一定有peak，反之亦然。

from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, A: List[int]) -> int:
        if not A:
            return -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < A[mid - 1] and A[mid] > A[mid + 1]:
                end = mid
            else:
                start = mid

        if A[start] > A[start - 1] and A[start] > A[start + 1]:
            return start
        elif A[end] > A[end - 1] and A[end] > A[end + 1]:
            return end
        else:
            return mid



from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        if not a:
            return -1
        left, right = 0, len(a) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if a[mid] > a[mid-1] and a[mid] > a[mid+1]:
                return mid
            # 如果切到的 mid 在上升区间，那么就往它的右边继续搜索。 
            if a[mid] > a[mid-1]:
                left = mid
            # 其他情况都在左边
            else:
                right = mid
        return -1