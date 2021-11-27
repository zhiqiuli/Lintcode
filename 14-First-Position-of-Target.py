# https://www.lintcode.com/problem/14/description

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        start, end = 0, len(nums)-1
        
        # 1
        while start + 1 < end:
            
            # 2
            mid = start + int((end-start)/2)

            # 3 如果nums[mid] >= target,则题解一定在左边，否则题解在右边
            # x x x x o o o
            #         ^
            if target <= nums[mid]:
                end = mid
            else:
                start = mid
        
        # 4
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
