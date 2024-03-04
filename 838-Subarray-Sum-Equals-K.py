'''
计算Prefix_sum的过程中，
用HashMap 记录当前prefix_sum出现的次数，
当prefix_sum - k 出现在HashMap中，叠加count
时间复杂度为O(n)
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0 
        prefix_sum = 0
        prefix_sum_to_times = {0: 1}
        
        for num in nums:
            
            prefix_sum += num 

            '''
            consider k = 3
            6
            [....][.........]
            6
            [..........][...]
            6
            [............][.]
            so prefix_sum_to_times[6] = 3
            9
            [...............]
            therefore prefix_sum_to_times[9 - 3] = 3
            count += prefix_sum_to_times[9 - 3]
            '''
            
            if prefix_sum - k in prefix_sum_to_times:
                
                count += prefix_sum_to_times[prefix_sum - k]
                
            if prefix_sum in prefix_sum_to_times:
                
                prefix_sum_to_times[prefix_sum] += 1 
                
            else:
                
                prefix_sum_to_times[prefix_sum] = 1 
            
        return count
