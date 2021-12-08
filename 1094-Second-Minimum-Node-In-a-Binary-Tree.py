# https://www.lintcode.com/problem/1094/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """
    def findSecondMinimumValue(self, root):
        res = []
        self.helper(root,res)
        if len(res) < 2:
            return -1
        return sorted(res)[1]
    
    def helper(self, root, res):
        if root is None:
            return 
        if root.val not in res:
            res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)
        return
