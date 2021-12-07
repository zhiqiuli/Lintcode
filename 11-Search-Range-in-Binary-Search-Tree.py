# https://www.lintcode.com/problem/11/description?_from=collection&fromId=161

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        res = [] # 使用一个类似global variable的变量
        self.helper(root, k1, k2, res)
        return res
    
    def helper(self, root, k1, k2, res):
        if root is None:
            return
        
        # 如果目前node數值<k1, 表示左節點必<k1,不必往下遍歷 
        if root.val > k1:
            self.helper(root.left , k1, k2, res)
        # 符合條件 加入res
        if k1 <= root.val <= k2:
            res.append(root.val)
        # 同上 若node數值>k2, 表示右節點必>k2, 不必往下遍歷
        if root.val < k2:
            self.helper(root.right, k1, k2, res)
        
        return
