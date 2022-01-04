"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        if not root:
            return 0
        return self.dfs(0, root)
    
    def dfs(self, curr_level, root):
        if root is None:
            return curr_level
        
        left_res  = self.dfs(curr_level, root.left)
        right_res = self.dfs(curr_level, root.right)

        return max(left_res, right_res) + 1
