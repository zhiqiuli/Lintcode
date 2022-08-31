'''
九章quick select 模板 -  LeetCode 215. Kth Largest Element in an Array

The time complexity for the average case for quick select is O(n) (reduced from O(nlogn) — quick sort).
The worst case time complexity is still O(n²), it happens when always picks the largest/smallest as the pivot.
But by using a random pivot , the worst case can be avoided in most cases.
So, on an average quick select provides a O(n) solution to find the kth largest/smallest element in an unsorted list.
'''

class Solution:
 def findKthLargest(self, nums: List[int], k: int) -> int:
     # kth larget = n - k th smallest
     return self.partition(nums, 0, len(nums) - 1, len(nums) - k) # 如果降序 self.partition(..., k)

 def partition(self, nums, start, end, k):
     # find kth smallest element in nums, here k is representing the index, and it starts from 0
     # only consider the index [start : end]
     # the following if ... return is not necessary
     if start >= end:
        return nums[k]
     l, r = start, end
     p = nums[(l + r) // 2]
     while l <= r:
         while l <= r and nums[l] < p: # 如果是降序 nums[l] > p (注意!这里是绝对大于>)
             l += 1
         while l <= r and nums[r] > p: # 如果是降序 nums[r] < p
             r -= 1
         if l <= r:
             nums[l], nums[r] = nums[r], nums[l]
             l += 1; r -= 1
     # right <= left by stoping condition
     if k <= r:
         return self.partition(nums, start, r, k)
     if k >= l:
         return self.partition(nums, l, end, k)
     return nums[k] # (注意!这里需要return[k])

'''
quick sort 模板 - LeetCode 912. Sort an Array
'''

class Solution:
 def sortArray(self, nums: List[int]) -> List[int]:
     self.quick_sort(nums, 0, len(nums) - 1)
     return nums 

 def quick_sort(self, nums, start, end):
     if start >= end: return
     l, r = start, end
     m = (l + r) // 2
     target = nums[m] # NOTE: 必须保存在单独变量中，如果直接使用nums[m]，在while循环中会nums[m]会发生变化。
     while l <= r:
         while l <= r and nums[l] < target:
             l += 1
         while l <= r and nums[r] > target:
             r -= 1
         if l <= r:
             nums[l], nums[r] = nums[r], nums[l]
             l += 1; r -= 1
     self.quick_sort(nums, start, r)
     self.quick_sort(nums, l, end)
