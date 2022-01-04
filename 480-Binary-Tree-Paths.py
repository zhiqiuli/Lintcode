"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if not root: return []
        res = []
        self.dfs(root, [str(root.val)], res)
        res_str = []
        for i in res:
            s = '->'.join(i)
            res_str.append(s)
        return res_str

    def dfs(self, root, path, res):
        if not root.left and not root.right:
            res.append(path[:])
            return
        if root.left:
            self.dfs(root.left ,  path + [str(root.left.val )], res)
        if root.right:
            self.dfs(root.right,  path + [str(root.right.val)], res)
