"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

###
### 使用纯 Divide & Conquer 的方法
### 切记D&C时不需要全局变量，也尽量避免全局变量
###
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        _, _, node = self.helper(root)
        return node

    def helper(self, root):
        if root is None:
            return 0, sys.maxsize, None
        
        left_sum , left_min , left_node  = self.helper(root.left )
        right_sum, right_min, right_node = self.helper(root.right)

        sum_of_root = left_sum + right_sum + root.val

        if left_min  == min(left_min, right_min, sum_of_root):
            return sum_of_root, left_min , left_node # 要点是返回三个值 分别是当前node sum，当前node的最小值，当前node最小值的node
 
        if right_min == min(left_min, right_min, sum_of_root):
            return sum_of_root, right_min, right_node
        
        return sum_of_root, sum_of_root, root
