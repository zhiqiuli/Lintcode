'''
先对于加热器数组排序。
对于每个房屋i，在加热器数组里使用二分查找找到距离房屋i最近的加热器的位置，
最后的答案为所有房屋答案的最大值。
'''
class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        res = 0
        for house in houses:
            res = max(res, self.findNearest(house, heaters))
        return res
    
    def findNearest(self, house, heaters):
        left  = 0
        right = len(heaters) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if heaters[mid] == house:
                return 0
            elif heaters[mid] > house:
                right = mid
            else:
                left = mid
        return min(abs(heaters[left]  - house),
                   abs(heaters[right] - house))
