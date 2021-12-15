https://www.lintcode.com/problem/839/description

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        index1, index2 = 0, 0

        ans = []

        while index1 < len(list1) and index2 < len(list2):
            a = list1[index1]
            b = list2[index2]

            #如果a左端点较小，说明a将被加入ans中，
            #所以令now = a，同时将i加一以便后面继续加入
            #如果b左端点较小，也类似操作
            if a.start <= b.start:
                now     = a
                index1 += 1
            else:
                now     = b 
                index2 += 1
            
            if not ans:
                ans.append(now)
            else:
                self.merge(ans, ans[-1], now)
            
        while index1 < len(list1):
            self.merge(ans, ans[-1], list1[index1])
            index1 += 1

        while index2 < len(list2):
            self.merge(ans, ans[-1], list2[index2])
            index2 += 1
        
        return ans
    
    def merge(self, ans, a, b):
        if a.end < b.start: # 如果last与now不相交，那直接将now加进ans即可
            ans.append(b)
        else: # 更新最后一个区间
            ans[-1].end = max(a.end, b.end)
