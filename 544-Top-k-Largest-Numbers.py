'''
保存所有元素 maxheap
'''
import heapq

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        h = []
        for num in nums:
            heapq.heappush(h, -num)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h))
        return [-i for i in res]
      
 '''
 保存k元素 minheap
 '''
import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        h = []
        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
                continue
            if num > h[0]:
                heapq.heappush(h, num)
                heapq.heappop(h)
        return sorted(h, reverse=True)
