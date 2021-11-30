# https://www.lintcode.com/problem/608/description?_from=collection&fromId=161
'''
标准2Sum模版
'''
class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if not nums:
            return []
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return []
