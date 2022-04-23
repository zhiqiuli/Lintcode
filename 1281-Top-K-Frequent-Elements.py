# METHOD 1
# COUNT + HEAPQ

class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
             we will sort your return value in output
    """
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        import heapq

        topK = []
        heapq.heapify(topK)
        for key in count.keys():
            heapq.heappush(topK, (count[key], key))
            if len(topK) > k:
                heapq.heappop(topK)
        
        res = [i for _, i in topK]
        
        return res


# METHOD 2
# COUNT + SORTING

class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
             we will sort your return value in output
    """
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq_ranking = [(i, k) for i, k in count.items()]
        freq_ranking = sorted(freq_ranking, key=lambda x:x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(freq_ranking[i][0])

        return res


# METHOD 3
# COUNT + SORTING
from typing import (
    List,
)

import heapq

class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
             we will sort your return value in output
    """
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        vals = list(count.keys())

        self.quick_sort(vals, count, 0, len(vals) - 1, k)

        return vals[:k]
    
    def quick_sort(self, nums, count_dict, start, end, k):
        left, right = start, end
        
        if left >= right:
            return
        
        pivot = count_dict[nums[(left + right) // 2]]

        while left <= right:

            while left <= right and count_dict[nums[left]] > pivot:
                left += 1

            while left <= right and count_dict[nums[right]] < pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left  += 1
                right -= 1

        if k <= right:
            return self.quick_sort(nums, count_dict, start, right, k)

        if k >= left:
            return self.quick_sort(nums, count_dict, left, end, k)
