# 双指针算法
class Solution:
    """
    @param nums: the given array
    @return:  the number of triplets chosen from the array that can make triangles
    """
    def triangleNumber(self, nums):
        # Write your code here
        nums = sorted(nums) # nlog(n)
        total = 0
        for k in range(2, len(nums)):
            left, right = 0, k - 1
            while left + 1 <= right:
                if nums[left] + nums[right] > nums[k]:
                    total += (right - left)
                    right -= 1
                else:
                    left  += 1
        return total
