# https://www.lintcode.com/problem/587/description?_from=collection&fromId=161

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0
            
        nums.sort()

        count = 0
        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] + nums[end] == target:
                count += 1
                start += 1
                end   -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end]   == nums[end + 1]:
                    end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return count
