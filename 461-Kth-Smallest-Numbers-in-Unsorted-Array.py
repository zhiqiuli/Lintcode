# https://www.lintcode.com/problem/461/description?_from=collection&fromId=161
'''
采用QuickSort的模版
'''
class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        n = len(nums)
        # 数组从0开始标号，要传k - 1
        return self.partition(nums, 0, n - 1, k - 1)
    
    def partition(self, nums, start, end, k):
        left, right = start, end
        pivot = nums[left]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # 注意此时right < left，如果第k在左侧(<=right)，搜索左侧的范围(<=right)，否则搜索右侧(>=left)。
        if k <= right:
            self.partition(nums, start, right, k)
        if k >= left:
            self.partition(nums,  left,  end, k)
        return nums[k]
