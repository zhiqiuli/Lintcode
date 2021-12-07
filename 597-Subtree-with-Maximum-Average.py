# https://www.lintcode.com/problem/597/?_from=collection&fromId=161

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
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        node, _, _, _ = self.helper(root)
        return node
    
    def helper(self, root):
        if root is None:
            return None, 0, 0, -sys.maxsize
        
        left_node , left_total , left_count , left_max  = self.helper(root.left)
        right_node, right_total, right_count, right_max = self.helper(root.right)

        cur_total   = root.val + left_total + right_total
        count_total = left_count + right_count + 1
        cur_avg     = cur_total / count_total

        if left_max  == max(left_max, right_max, cur_avg):
            return left_node , cur_total, count_total,  left_max
        if right_max == max(left_max, right_max, cur_avg):
            return right_node, cur_total, count_total, right_max
        return root, cur_total, count_total, cur_avg
