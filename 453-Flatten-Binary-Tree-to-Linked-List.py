# https://www.lintcode.com/problem/453/description?_from=collection&fromId=161

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        return self.helper(root)
    
    # restructure and return last node in pre-order 
    def helper(self, root):
        if root is None:
            return None

        # 假设左边右边已经排序好了
        left_last  = self.helper(root.left)
        right_last = self.helper(root.right)

        # 将left_last的右边的node接到root.right
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        
        # return的顺序很重要 right, left and root
        return right_last or left_last or root
