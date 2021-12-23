"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if root is None:
            return 0
        left_min_dep  = self.minDepth(root.left )
        right_min_dep = self.minDepth(root.right)
        if left_min_dep == 0 or right_min_dep == 0:
            return left_min_dep + right_min_dep + 1
        return min(left_min_dep, right_min_dep) + 1
