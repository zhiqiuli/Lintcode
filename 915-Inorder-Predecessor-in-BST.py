# https://www.lintcode.com/problem/915/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        if root is None:
            return None
            
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        prev  = None
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack and stack[-1] == p:
                return prev
            else:
                prev = stack[-1]
        return None
