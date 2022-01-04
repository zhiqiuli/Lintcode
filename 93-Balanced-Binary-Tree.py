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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        if not root:
            return True
        _, is_bal = self.dfs(0, root)
        return is_bal

    def dfs(self, curr_level, root):
        if root is None:
            return curr_level, True

        left_level , left_bal  = self.dfs(curr_level, root.left )
        right_level, right_bal = self.dfs(curr_level, root.right)

        is_bal = True if abs(left_level - right_level) <= 1 and left_bal and right_bal else False

        return max(left_level, right_level) + 1, is_bal
