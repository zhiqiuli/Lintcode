"""
Sweep line的经典题
(1,7) (2, 8)
Create an event list (1,-1), (7,1), (2,-1), (8,1)
Sorted by the first element then second element (1,-1), (2,-1), (7,1), (8,1)
Count the elements are 1, 2, 1, 0 return 2
 
(1,3),(2,3),(3,4)
Create an event list (1,-1),(3,1),(2,-1),(3,1),(3,-1),(4,1)
Sorted by 1st element then second element (1,-1),(2,-1),(3,-1),(3,1),(3,1), (4,1)
Count the elements are 1, 2, 3, 2, 1, 0 return 3
"""

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
    @param intervals: The intervals
    @return: The answer
    """
    def digital_coverage(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, -1))
            events.append((interval.end  ,  1))
        
        events.sort()

        max_count = 0
        count = 0

        for node, check in events:
            if check == -1:
                count += 1
            else:
                count -= 1
            if count > max_count:
                max_count = count
                res = node
        
        return res

        print(events)
        return 2
