# Details in 862. Shortest Subarray with Sum at Least K

from collections import deque

from typing import (
    List,
)

class Solution:
    """
    @param a: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, a: List[int], k: int) -> int:
        presum = [0] * (len(a) + 1)
        for i in range(1, len(a) + 1):
            presum[i] = presum[i-1] + a[i-1]
        queue = deque()
        res = sys.maxsize
        for i in range(len(a) + 1):
            while len(queue) != 0 and presum[queue[-1]] > presum[i]:
                queue.pop()
            while len(queue) != 0 and presum[i] - presum[queue[0]] >= k:
                res = min(res, i - queue[0])
                queue.popleft()
            queue.append(i)
        return -1 if res == sys.maxsize else res
