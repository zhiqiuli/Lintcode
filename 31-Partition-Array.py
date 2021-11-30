# https://www.lintcode.com/problem/31/description?_from=collection&fromId=161
'''
Partition 模版

while left <= right:
	while left <= right and nums[left] 应该在左边：
		left += 1
	while left <= right and nums[right] 应该在右边：
		right -= 1

	if left <= right:
		# 找到一个不该在左侧的和不该在右边的，交换他们
		nums[left], nums[right] = nums[right], nums[left]
		left += 1
		right -= 1

- Partition 是非左即右
- Quicksort 等于的时候需要特殊处理
如果Quicksort如果非左即右的话，考虑全是1 1 ... 1的数组，无法进行partition
- Quick Select和Quick Sort的代码几乎一摸一样
- Kth largest element (*)
- Partition缺点 - 不稳定，没有办法保证同一类的<k或者>=k （？不太理解）
- Quick Sort & Merge Sort
- Linked List Cycle & Intersection of Linked List
'''

class Solution:

    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left  += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
		        # 找到一个不该在左侧的和不该在右边的，交换他们
                nums[left], nums[right] = nums[right], nums[left]
                left  += 1
                right -= 1

        return left # remember always return left
