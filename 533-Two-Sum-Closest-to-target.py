# https://www.lintcode.com/problem/533/?_from=collection&fromId=161

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        if not nums:
            return 0
        nums.sort()
        
        diff = sys.maxsize
        
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right] - target

            diff = min(abs(s), diff)
            if s > 0:
                right -= 1
            else:
                left += 1
        
        return diff
