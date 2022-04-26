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

"""
METHOD 1
"""
class Solution:
    """
    @param root: the root node
    @param l: an integer
    @param r: an integer
    @return: the sum
    """
    def range_sum_b_s_t(self, root: TreeNode, l: int, r: int) -> int:
        stack = []
        res = 0
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            node = stack.pop()
            if l <= node.val <= r: res += node.val
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
                    
        return res

      
"""
METHOD 2
"""
class Solution:
    def __init__(self):
        self.res = 0
    """
    @param root: the root node
    @param l: an integer
    @param r: an integer
    @return: the sum
    """
    def range_sum_b_s_t(self, root: TreeNode, l: int, r: int) -> int:
        queue = []
        res = 0
        while root:
            queue.append(root)
            root = root.left
        while queue:
            node = queue.pop()
            if node.val >= l and node.val <= r:
                res += node.val
            if node.right:
                node = node.right
                while node:
                    queue.append(node)
                    node = node.left
        return res
