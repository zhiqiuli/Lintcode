from typing import (
    List,
)
import heapq
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
            
        # h是一个priority queue，其保存的是[-1,0],[-2,1],[-7,2]
        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h)
        res = [-h[0][0]] # res=[7]

        for i in range(k, len(nums)):

            heapq.heappush(h, (-nums[i], i))
            
            # 当最大值出现在范围外时，需要pop出去，否则不会影响结果
            # 比方说 k=2， h=[-7,0], [-2,1], new [-1,2]
            # h[0]=[-7,0], i=2, h[0][1]=0 <= i-k = 0, 需要去掉h[0]
            while h[0][1] <= i - k:
                heapq.heappop(h)
            
            res.append(-h[0][0])
        
        return res