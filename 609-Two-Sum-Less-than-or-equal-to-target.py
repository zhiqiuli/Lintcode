# https://www.lintcode.com/problem/609/?_from=collection&fromId=161
'''
相反双指针 - 和2Sum模版很接近
'''

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        if not nums:
            return 0
        
        nums.sort()
        count = 0

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        
        return count
