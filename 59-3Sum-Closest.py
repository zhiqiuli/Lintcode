class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        numbers  = sorted(numbers) # O(nlogn)
        min_dist = sys.maxsize
        for k in range(2, len(numbers)):
            left, right = 0, k - 1
            while left < right:
                tmp_sum = numbers[left] + numbers[right] + numbers[k]
                dist    = abs(tmp_sum - target)
                if dist < min_dist:
                    res      = tmp_sum
                    min_dist = dist
                if tmp_sum > target:
                    right -= 1
                else:
                    left  += 1
        return res
