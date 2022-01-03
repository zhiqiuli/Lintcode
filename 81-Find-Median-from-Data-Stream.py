import heapq

class Solution:
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    """
    @param val: a num from the data stream.
    @return: nothing
    """
    def add(self, val: int):

        if len(self.minheap) == 0:
            heapq.heappush(self.minheap,  val)
            return

        if val > self.minheap[0]:
            heapq.heappush(self.minheap,  val)
        else:
            heapq.heappush(self.maxheap, -val)

        if len(self.minheap) - len(self.maxheap) == 2:
            element =  heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -element)
            return

        if len(self.maxheap) - len(self.minheap) == 2:
            element = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,  element)
            return

    """
    @return: return the median of the all numbers
    """
    def getMedian(self) -> int:
        if len(self.minheap) == len(self.maxheap):
            return -self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return  self.minheap[0]
        else:
            return -self.maxheap[0]
