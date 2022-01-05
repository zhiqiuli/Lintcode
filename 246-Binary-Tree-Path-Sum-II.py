"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        if not root:
            return []
        res = []
        self.traversal(root, res, target)
        return res
    
    def traversal(self, root, res, target):
        if not root:
            return
        
        self.dfs(root, res, [], target)
        
        self.traversal(root.left , res, target)
        self.traversal(root.right, res, target)

    def dfs(self, root, res, path, target):
        if not root:
            return
        
        path.append(root.val)

        if target == root.val:
            res.append(path[:])

        self.dfs(root.left , res, path, target - root.val)
        self.dfs(root.right, res, path, target - root.val)
        path.pop()
