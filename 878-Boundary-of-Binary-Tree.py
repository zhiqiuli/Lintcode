from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundary_of_binary_tree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
            
        left_boundary  = self.find_left_boundary (root.left )
        leaves         = self.find_leaves        (root)
        right_boundary = self.find_right_boundary(root.right)
        if left_boundary  and leaves and left_boundary[-1] == leaves[0]:
            leaves = leaves[1:]
        if right_boundary and leaves and right_boundary[-1] == leaves[-1]:
            leaves = leaves[:-1]
        return [root.val] + left_boundary + leaves + right_boundary[::-1]

    def find_leaves(self, root):
        leaves = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaves
    
    def find_left_boundary(self, root):
        left_boundary = []
        while root:
            left_boundary.append(root.val)
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                break
        return left_boundary

    def find_right_boundary(self, root):
        right_boundary = []
        while root:
            right_boundary.append(root.val)
            if root.right:
                root = root.right
            elif root.left:
                root = root.left
            else:
                break
        return right_boundary
