https://www.lintcode.com/problem/612/description?_from=collection&fromId=161
  
import heapq

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        h = []
        for p in points:
            dist = (p.x - origin.x) ** 2 + (p.y - origin.y) ** 2
            heapq.heappush(h, (dist, p.x, p.y)) # If two points have the same Euclidean distance, they are sorted by x values. If the x value is the same, then we sort it by the y value.
        
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(h)
            res.append(Point(x, y))
        
        return res
