from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return []

        # 按照区间start进行排序
        intervals = sorted(intervals, key=lambda x:x.start)
        last_interval = intervals[0]
        res = []
        
        # 如果两段区间有交集的话，合并两段区间
        # 没有的话，将最后的区间加入答案，并令新的区间作为最后的区间
        for i in range(1, len(intervals)):
            if self.has_intersect(last_interval, intervals[i]):
                last_interval = self.merge_intervals(last_interval, intervals[i])
            else:
                res.append(last_interval)
                last_interval = intervals[i]
        res.append(last_interval)
        return res
    
    # 关键点：判断区间是否有交集，要满足较大的start小于等于较小的end
    def has_intersect(self, a, b):
        return max(a.start, b.start) <= min(a.end, b.end)
    
    def merge_intervals(self, a, b):
        return Interval(min(a.start, b.start), max(a.end, b.end))
      

###
### soltion with space O(1)
###   
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return []

        # 按照区间start进行排序
        intervals = sorted(intervals, key=lambda x:x.start)
        last_interval = intervals[0]
        #res = []
        
        # 如果两段区间有交集的话，合并两段区间
        # 没有的话，将最后的区间加入答案，并令新的区间作为最后的区间
        i = 1
        j = 0
        while i < len(intervals):
            if self.has_intersect(last_interval, intervals[i]):
                last_interval = self.merge_intervals(last_interval, intervals[i])
            else:
                #res.append(last_interval)
                intervals[j] = last_interval
                j += 1
                last_interval = intervals[i]
            i += 1
        #res.append(last_interval)
        intervals[j] = last_interval
        j += 1
        return intervals[:j]
    
    # 关键点：判断区间是否有交集，要满足较大的start小于等于较小的end
    def has_intersect(self, a, b):
        return max(a.start, b.start) <= min(a.end, b.end)
    
    def merge_intervals(self, a, b):
        return Interval(min(a.start, b.start), max(a.end, b.end))
