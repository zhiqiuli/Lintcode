"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

###
### recursive
###
# https://www.lintcode.com/problem/85/description?_from=collection&fromId=161
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        return self.helper(root, node)
    
    def helper(self, root, node):
        if root is None:
            return node
        if node.val > root.val:
            root.right = self.helper(root.right, node)
        if node.val < root.val:
            root.left  = self.helper(root.left , node)
        return root


###
### non-recursive
###
# https://www.lintcode.com/problem/85/description?_from=collection&fromId=161
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if root is None:
            return node
        
        curr = root
        while curr != node:
            if node.val > curr.val:
                if curr.right is None:
                    curr.right = node
                curr = curr.right
            else:
                if curr.left is None:
                    curr.left = node
                curr = curr.left

        return root
