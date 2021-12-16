# https://www.lintcode.com/problem/52/description

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]: # 从右到左，找到第一个严格下降的数i，nums[i+1]之后为non-increasing
            i -= 1
        if i != -1: # 整个数列如果已经是non increasing 则直接反转
            j = i + 1
            while j < len(nums) and nums[i] < nums[j]: # 从i+1开始，找到第一个j（最小的nums[j]）并且nums[j]>nums[i]严格
                j += 1
            j -= 1
            nums[i], nums[j] = nums[j], nums[i] # 交换
        i = i + 1
        j = len(nums) - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums
