# https://www.lintcode.com/problem/175/?_from=collection&fromId=161

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        self.helper(root)

    def helper(self, root):
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.helper(root.left )
        self.helper(root.right)
