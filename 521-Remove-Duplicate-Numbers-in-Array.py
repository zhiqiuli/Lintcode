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
