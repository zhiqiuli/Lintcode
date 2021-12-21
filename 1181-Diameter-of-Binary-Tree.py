"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        diameter, _ = self.dfs(root)
        return diameter

    def dfs(self, root):
        if root is None:
            return 0, 0
        left_diameter , left_longest  = self.dfs(root.left )
        right_diameter, right_longest = self.dfs(root.right)
        # 最长的dimeter不一定会经过root，需要保存左右最深长度以及左右的最长diameter
        return max(left_diameter, right_diameter, left_longest + right_longest), 1 + max(left_longest, right_longest)
