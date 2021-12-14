https://www.lintcode.com/problem/4/?_from=collection&fromId=161

'''
复杂度分析
时间复杂度：O(nlog(n))O(nlog(n))。弹出每个最小值时，时间复杂度都为堆的高度，因此时间复杂度为O(nlog(n))O(nlog(n))。
空间复杂度：O(n)O(n)。遍历n个丑数，并将每个丑数乘以2、3和5的结果存入堆中。堆和哈希表的元素个数都不会超过n * 3。
'''

import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        heap = []
        heapq.heappush(heap, 1)

        seen = set()
        seen.add(1)
        
        factors = [2, 3, 5]
        curr_ugly = 1
        
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            for f in factors:
                curr_ugly_ = f * curr_ugly
                if curr_ugly_ not in seen:
                    # O(log N) Push / O(log N) Pop / O(1) Top
                    seen.add(curr_ugly_)
                    heapq.heappush(heap, curr_ugly_)
        
        return curr_ugly
