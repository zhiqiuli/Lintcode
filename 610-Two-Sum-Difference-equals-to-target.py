https://www.lintcode.com/problem/610/description?_from=collection&fromId=161
  
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        target = abs(target)
        left, right = 0, 0
        while right < len(nums):
            if left == right:
                right += 1
            if nums[right] - nums[left] == target:
                return [nums[left], nums[right]]
            elif nums[right] - nums[left] < target:
                right += 1
            else:
                left  += 1
