class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums) # 结尾是dp[i]的LIS是多少
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    
* [1,2,8] and [3,4,5] have the same length, which one is better?
  [3,4,5] is better because the [6] can be added on [3,4,5] but not on [1,2,8].
* [1,2,5] and [3,4,5] are the same at length 3.
* [1,2] is better than [3,4] at length 2.
* Only the last number matter.

###
### dp[i] the smallest ending number of a subsequency that has length i+1
###

1. Extend the longest subseq
2. Replace a number to generate a better subseq

Example:

nums 4 5 1 2 8 5 6

dp
[3] 长度为1的subseq的结尾最小元素为3
[3,4] // [3], [*,4]
[1,4]
[1,2] 长度为2的subseq的结尾的最小元素为2 // [1], [*,2]
[1,2,8] // [1], [*,2], [*,*,8]
[1,2,5] // [1]
[1,2,5,6] // [1], [*,2], [*,5]

* dp[]是单调递增的序列，使用binary search找到最合适的位置
* 最终的答案就是 len(dp)

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0

        dp = [sys.maxsize] * len(nums)

        for num in nums:
            index = self.helper(num, dp)
            dp[index] = num
        
        return len([i for i in dp if i != sys.maxsize])
    
    def helper(self, target, A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target: # 注意是>=。譬如说[1]，target是1，不需要进行append。
                end = mid
            else:
                start = mid
        
        if A[start] >= target: return start
        if A[end]   >= target: return end
