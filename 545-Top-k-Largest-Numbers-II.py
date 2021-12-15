https://www.lintcode.com/problem/545/description?_from=collection&fromId=161
  
'''
保存k个元素

490ms
Time Cost

6.06MB
Memory Cost

93.40%
Beats
'''
import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.h    = []
        self.k    = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.h) < self.k:
            heapq.heappush(self.h, num)
            return
        if num > self.h[0]:
            heapq.heappop(self.h)
            heapq.heappush(self.h, num)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return sorted(self.h, reverse=True)


'''
保存所有的元素

535 ms
time cost

5.99 MB
memory cost

Your submission beats
28.80 %
Submissions
'''
import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.h = []
        self.k = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heapq.heappush(self.h, -num)

    """
    @return: Top k element
    """
    def topk(self):
        res = []
        local_h = self.h[:]
        k = 0
        while local_h and k < self.k:
            res.append(-heapq.heappop(local_h))
            k += 1
        return res
