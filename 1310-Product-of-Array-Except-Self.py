###
### method 1
###
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def product_except_self(self, nums: List[int]) -> List[int]:

        products = [1] * len(nums)
        
        leading = 1
        for i, num in enumerate(nums):
            products[i] = leading
            leading *= num
        
        trailing = 1
        for i, num in reversed(list(enumerate(nums))):
            products[i] *= trailing
            trailing *= num
        
        return products
      
      
      
###
### method 2
###
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def product_except_self(self, nums: List[int]) -> List[int]:
        # 全是0
        if len(set(nums)) == 1 and nums[0] == 0:
            return [0] * len(nums)
        
        # 有两个或以上0
        if nums.count(0) > 1:
            return [0] * len(nums)
        
        # 有一个0
        if nums.count(0) == 1:
            all_prod = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    all_prod *= nums[i]
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = all_prod
                else:
                    nums[i] = 0
            return nums

        # 完全没有0
        all_prod = 1
        for i in range(len(nums)):
            all_prod *= nums[i]
        for i in range(len(nums)):
            nums[i] = all_prod // nums[i]
        return nums
