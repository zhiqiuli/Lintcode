### Option 1
class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def find_pairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i, j = 0, 1
        res = 0
        while j < len(nums):

            if nums[j] - nums[i] > k:
                i += 1

            elif nums[j] - nums[i] < k:
                j += 1

            else:
                res += 1

                i += 1
                j += 1
            
                # remove the duplicated
                while j < len(nums) and nums[j] == nums[j - 1]:
                    j += 1
                
                while i and i < j and nums[i] == nums[i - 1]:
                    i += 1
            
            # to prevent it runs out of range
            if i == j:
                j += 1

        return res

### Option 2
class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def find_pairs(self, nums: List[int], k: int) -> int:
        # Write your code here
        visited = {}
        for num in nums:
            if num not in visited:
                visited[num] = 1
            else:
                visited[num] += 1
 
        if k == 0:
            res = 0
            for key in visited.keys():
                if visited[key] > 1:
                    res += 1
            return res
 
        res = 0
        for key in visited.keys():
            if key - k in visited.keys():
                res += 1
 
        return res
