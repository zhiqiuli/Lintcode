# https://www.lintcode.com/problem/632

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        _, node = self.helper(root)
        return node
    
    def helper(self, root):
        if root is None:
            return -sys.maxsize, None
        
        left_max,  left_node  = self.helper(root.left )
        right_max, right_node = self.helper(root.right)

        if left_max  == max(root.val, left_max, right_max):
            return left_max, left_node
        if right_max == max(root.val, left_max, right_max):
            return right_max, right_node
        return root.val, root
