# https://www.lintcode.com/problem/628
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        _, _, node = self.dfs(root)
        return node

    def dfs(self, root):
        if root is None:
            # Current max, Current sum, Subtree with current max
            return -sys.maxsize, 0, None
        
        left_max,  left_sum,  left_node  = self.dfs(root.left )
        right_max, right_sum, right_node = self.dfs(root.right)

        curr_sum = left_sum + right_sum + root.val

        if left_max == max(left_max, right_max, curr_sum):
            return left_max , curr_sum, left_node
        if right_max == max(left_max, right_max, curr_sum):
            return right_max, curr_sum, right_node
        return curr_sum, curr_sum, root
