from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuous_subarray_sum_i_i(self, a: List[int]) -> List[int]:
        # write your code here
        # find [xxxxoooooxxx] - case 1
        left_max, right_max, sum_max = self.find_max_subarray(a)
        # find [ooooxxxxxooo] - case 2
        left_min, right_min, sum_min = self.find_max_subarray([-i for i in a])

        print(left_max, right_max, sum_max)
        print(left_min, right_min, sum(a) + sum_min)
        
        # 第二部分是说所有元素加和以后是最小的，或者可以使用 right_min - left_min + 1 = n
        # 从case 1和case 2中选择最大的
        if sum_max >= sum(a) + sum_min or sum(a) + sum_min == 0:
            return [left_max, right_max]

        return [right_min + 1, left_min - 1]


    def find_max_subarray(self, a):
        left = right = left_tmp = 0
        sum = 0
        max_sum = a[0]
        for right_tmp in range(len(a)):
            if sum >= 0:
                sum += a[right_tmp]
            else:
                sum = a[right_tmp]
                left_tmp = right_tmp

            if sum > max_sum:
                left    = left_tmp
                right   = right_tmp
                max_sum = sum
        
        return left, right, max_sum