# https://www.lintcode.com/problem/539/description?_from=collection&fromId=161
'''
维护顺序 - 同向双指针，并不能保证最少的write的次数，但是很好理解
'''
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if not nums:
            return []
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1        
        return nums
