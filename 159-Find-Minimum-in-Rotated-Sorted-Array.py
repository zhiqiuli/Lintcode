# https://www.lintcode.com/problem/159/description

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        # the first position where <= the last number
        target = nums[-1]

        # 1
        while start + 1 < end:

            # 2
            mid = start + int((end - start)/2)

            # 3 The basic idea is to find the first position where <= the last number
            if nums[mid] <= target:
                end = mid
            else:
                start = mid

        if nums[start] > nums[end]:
            return nums[end]
        else:
            return nums[start]
