'''
使用 heapq 的方法
最快，因为不需要创建额外空间。
时间复杂度和其他的算法一致，都是O(N logK)，N是所有元素个数。

[0 8 9 10 11]
[1 3 5 7]
[2 4 6]
'''
https://www.lintcode.com/problem/486/description?_from=collection&fromId=161

import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        results = []
        h = []
        for index, row in enumerate(arrays):
            if len(row) == 0:
                continue
            heapq.heappush(h, (row[0], index, 0)) # this heap stores tuples (1, 0, 0) (2, 1, 0) (0, 2, 0)
        
        while len(h):
            val, index, row = heapq.heappop(h)
            results.append(val)
            if row + 1 < len(arrays[index]): # everytime pop an the least number in the heap and move forwards
                heapq.heappush(h, (arrays[index][row + 1], index, row + 1))
        
        return results
