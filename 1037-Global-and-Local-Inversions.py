'''
第一步：首先思考全局逆序数和局部逆序数的定义，不管是哪种逆序数，都是这一对元素大小颠倒。理解什么是全局逆序数，就是相邻或者不相邻出现的逆序数，局部逆序数是指必须相邻的逆序数。当且仅当全局逆序数的i和j相差大于1时，这就只是一组全局逆序数，但不是局部逆序数。 
第二步：发现，局部逆序数一定是全局逆序数，而全局逆序数不一定是局部逆序数。所以问题的焦点就变成了是否能找出不是局部倒置的全局倒置。
第三步：为了和局部倒置区别开来，我们不能比较相邻的两个，而是至少要隔一个来比较。
'''
from typing import (
    List,
)

class Solution:
    """
    @param a: an array
    @return: is the number of global inversions is equal to the number of local inversions
    """
    def is_ideal_permutation(self, a: List[int]) -> bool:
        max_val = -1
        for i in range(2, len(a)):
            max_val = max(max_val, a[i-2])
            if max_val > a[i]:
                return False
        return True
