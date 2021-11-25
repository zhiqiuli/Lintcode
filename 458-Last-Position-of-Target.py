# https://www.lintcode.com/problem/458

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1

        # 1
        while start + 1 < end:

            # 2
            mid = start + int((end - start) / 2)

            # 3 和first position正好相反，判断start位置，并且保证nums[mid] <= target
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        
        # 4 一定要先返回end，再返回start
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1
