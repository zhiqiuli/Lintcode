from typing import (
    List,
)

class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    [3, 0, 6, 1, 5]
    sorted
    [0, 1, 3, 5, 6]
    n - i
    [5, 4, 3, 2, 1]

    至少5个paper被cited了0次
    至少4个paper被cited了1次
    至少3个paper被cited了3次 -》 答案
    至少2个paper被cited了5次
    至少1个paper被cited了6次
    """
    def h_index(self, citations: List[int]) -> int:
        citations = sorted(citations)
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0
