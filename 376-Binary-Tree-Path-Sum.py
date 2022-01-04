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
    def binaryTreePathSum(self, root, target):
        if not root:
            return []
        res = []
        self.dfs(root, target, root.val, [root.val], res)
        return res

    def dfs(self, root, target, curr_sum, path, res):
        if not root.left and not root.right:
            if curr_sum == target:
                res.append(path[:])
            return
        if root.left:
            self.dfs(root.left , target, curr_sum + root.left.val , path + [root.left.val ], res)
        if root.right:
            self.dfs(root.right, target, curr_sum + root.right.val, path + [root.right.val], res)
