https://www.lintcode.com/problem/138/description?_from=collection&fromId=161
  
# 某一段[l, r]的和为0，则其对应presum[l-1] = presum[r]
# index_hash存的是-1
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        index_hash = {0: -1}
        presum = 0
        for i, num in enumerate(nums):
            presum += num
            if presum in index_hash:
                return index_hash[presum] + 1, i
            index_hash[presum] = i
        return -1, -1
