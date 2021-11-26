# https://www.lintcode.com/problem/447/description
class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        
        k = 0
        if reader.get(k) == target:
            return k
        
        k = 1
        while reader.get(k) <= target:
            k = 2 * k
        
        # start 也可以是 kth / 2，但是我习惯比较保守的写法
        # 因为写为 0 也不会影响时间复杂度
        lo, hi = 0, 2 * k - 1

        # 1
        while lo + 1 < hi:
            
            # 2
            mid = lo + int((hi - lo) / 2)

            # 3 find the first target in the array
            if target <= reader.get(mid):
                hi = mid
            else:
                lo = mid
        
        # 4
        if reader.get(lo) == target:
            return lo
        if reader.get(hi) == target:
            return hi
        
        return -1
