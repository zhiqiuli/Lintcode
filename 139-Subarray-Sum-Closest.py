class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        prefix_sum = 0
        prefix_sum_list = [(0, -1)] # initialize
        for i in range(len(nums)): # O(N)
            prefix_sum += nums[i]
            # stores prefix_sum and index of position
            prefix_sum_list.append((prefix_sum, i))
        prefix_sum_list.sort() # sort O(N logN)
        print(prefix_sum_list)
        diff = sys.maxsize
        left_index  = -1
        right_index = -1
        for i in range(1, len(prefix_sum_list)): # O(N)
            if prefix_sum_list[i][0] - prefix_sum_list[i - 1][0] < diff:
                diff = prefix_sum_list[i][0] - prefix_sum_list[i - 1][0]
                # +1和initialize数据有关系，考虑当只有一个元素100时，[(0,-1), (177,0)] -> left = min(-1,0)+1 = 0 & right = max(-1,0) = 0
                left_index  = min(prefix_sum_list[i][1], prefix_sum_list[i - 1][1]) + 1
                right_index = max(prefix_sum_list[i][1], prefix_sum_list[i - 1][1])
        return [left_index, right_index]
