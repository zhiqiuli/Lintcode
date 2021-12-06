# https://www.lintcode.com/problem/900/description?_from=collection&fromId=161

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

'''
Remember BST property that target = 10.5
  5
 / \
4   9
'''

###
### non-recursive
###
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        upper, lower = root, root
        while root:
            if target > root.val:
                lower = root
                root  = root.right
            elif target < root.val:
                upper = root
                root  = root.left
            else:
                return root.val
        
        if abs(upper.val - target) > abs(target - lower.val):
            return lower.val
        return upper.val



###
### recursive 
###
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if root is None:
            return None
        
        lower = self.get_lower_bound(root, target)
        upper = self.get_upper_bound(root, target)

        if lower is None:
            return upper.val
        if upper is None:
            return lower.val

        if upper.val - target > target - lower.val:
            return lower.val
        return upper.val
    
    def get_lower_bound(self, root, target):
        # get the largest node that < target
        if root is None:
            return None
        
        if target < root.val:
            return self.get_lower_bound(root.left, target)
            
        lower = self.get_lower_bound(root.right, target)
        return root if lower is None else lower

    def get_upper_bound(self, root, target):
        # get the largest node that >= target
        if root is None:
            return None
        
        if target >= root.val:
            return self.get_upper_bound(root.right, target)
            
        upper = self.get_upper_bound(root.left, target)
        return root if upper is None else upper
