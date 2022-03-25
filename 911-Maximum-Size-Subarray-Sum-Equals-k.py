from typing import (
    List,
)

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def max_sub_array_len(self, nums: List[int], k: int) -> int:
        #     prefix_sum[i] - prefix_sum[e] = k
        #  => prefix_sum[e] = prefix_sum[i] - k
        dict = {0:-1}
        prefix_sum = 0
        leng = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in dict:
                # 题目要求的是maximum size subarray 只需要保存最前面的index位置
                leng = max(leng, i - dict[prefix_sum - k])
            if prefix_sum not in dict:
                dict[prefix_sum] = i
        return leng
