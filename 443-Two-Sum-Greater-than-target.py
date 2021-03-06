# https://www.lintcode.com/problem/443/?_from=collection&fromId=161
'''
2Sum模版
'''
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if not nums:
            return 0
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                count += (right - left)
                right -= 1
            else:
                left += 1
        
        return count
