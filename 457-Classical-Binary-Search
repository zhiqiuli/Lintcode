https://www.lintcode.com/problem/457/

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        # 要点1: start + 1 < end
        while start + 1 < end:
            
            # 要点2：start + (end - start) / 2
            mid = start + int((end - start)/2)
            
            # 要点3：=, <, > 分开讨论，mid 不+1也不-1
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                end = mid
            else:
                start = mid
                
        # 要点4: 循环结束后，单独处理start和end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
