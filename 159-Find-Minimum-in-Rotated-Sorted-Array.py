class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            # 此时数组已经排好序了，直接取第一个数即可
            if nums[left] <= nums[right]:
                return nums[left]
            # 此时数组肯定是rotated的，需要进一步判断，取存在最小值的部分即可
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])
    
    
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
