# https://www.lintcode.com/problem/95/solution?_from=collection&fromId=161

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        if root is None:
            return True
        
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        inorder = []

        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)

        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]:
                return False

        return True
