"""
This is how the height looks like

      1 (2)
    /   \
   2 (1) 3 (0)
 /  \
4(0) 5(0)

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, results):
        if root is None:
            return -1
        
        height = -1

        left_height  = self.helper(root.left , results)
        right_height = self.helper(root.right, results)

        height = max(left_height, right_height) + 1
        
        if height >= len(results):
            results.append([])
        results[height].append(root.val)

        return height
