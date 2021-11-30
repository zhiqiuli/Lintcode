# https://www.lintcode.com/problem/5/?_from=collection&fromId=161
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # 1 k^th largest input k - 1
        return self.QuickSelect(n - 1, nums, 0, len(nums) - 1)
    
    def QuickSelect(self, k, nums, start, end):
        # 2 define l, r without -1 and define pivot as nums[left]
        left, right = start, end
        pivot = nums[left]
        
        # 3 kth largest element - this is the only part changed if kth largest or kth smallest
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # 4 return partition
        if k <= right:
            self.QuickSelect(k, nums, start, right)
        if k >= left:
            self.QuickSelect(k, nums, left, end)
        
        # 5 remember to return nums[k]
        return nums[k]
