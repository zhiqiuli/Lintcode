"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        if not root:
            return []
        res = []
        self.dfs1(root, res, target)
        return res
    
    def dfs1(self, root, res, target):
        if not root:
            return
        visited = set()
        self.dfs2(root, res, [], visited, target)

        self.dfs1(root.left , res, target)
        self.dfs1(root.right, res, target)
    
    def dfs2(self, root, res, path, visited, target):
        #print(path)
        if (not root) or (root in visited):
            return
        path.append(root.val) # 先append path 再判断是否能加和target
        visited.add(root)
        if sum(path) == target:
            res.append(path[:])
        self.dfs2(root.left  , res, path, visited, target)
        self.dfs2(root.right , res, path, visited, target)
        self.dfs2(root.parent, res, path, visited, target)
        path.pop()
        visited.remove(root)
