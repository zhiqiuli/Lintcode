# https://www.lintcode.com/problem/585/description

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        # 1
        while start + 1 < end:
            
            # 2
            # mid + 1 保证不会越界
            # 因为 start 和 end 是 start + 1 < end
            mid = start + int((end-start)/2)

            # 3
            # find first index i so that nums[i] > nums[i + 1]
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid
        
        # 4
        if nums[start] > nums[end]:
            return nums[start]
        else:
            return nums[end]
