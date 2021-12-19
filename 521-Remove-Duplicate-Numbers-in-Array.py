class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if not nums: return 0
        visited = set([])
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] not in visited:
                visited.add(nums[i])
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return i

    
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if not nums: return 0
        if len(nums) == 1: return 1
        nums.sort() # 这个题只能用.sort()来做
        k = 0
        for i in range(1, len(nums)):
            print(i, k, nums)
            if nums[k] != nums[i]:
                k += 1
                nums[k], nums[i] = nums[i], nums[k]
        return k + 1
