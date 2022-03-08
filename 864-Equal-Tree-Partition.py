"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def checkEqualTree(self, root):
        return self.dfs(root)
    
    def dfs(self, root):
        if root is None:
            return False

        left_sum  = self.pathSum(root.left)
        right_sum = self.pathSum(root.right)

        if left_sum + root.val == right_sum or left_sum == right_sum + root.val:
            return True
        
        self.dfs(root.left)
        self.dfs(root.right)

        return False

    def pathSum(self, root):
        if root is None:
            return 0
        return root.val + self.pathSum(root.left) + self.pathSum(root.right)
