"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        if not root:
            return None
        left_node  = self.get_min_node(root)
        right_node = self.get_max_node(root)

        while left_node != right_node:
            pivot = left_node.val + right_node.val
            if pivot == n:
                return [left_node.val, right_node.val]
            elif pivot > n:
                right_node = self.get_predecessor(root, right_node)
            else:
                left_node  = self.get_successor  (root, left_node)
        return 
    
    def get_min_node(self, root):
        node = root
        while node.left:
            node = node.left
        return node

    def get_max_node(self, root):
        node = root
        while node.right:
            node = node.right
        return node
    
    # ...
    def get_successor(self, root, p):
        node, upper = root, None
        while node:
            if node.val > p.val:
                upper = node
                node = node.left
            else:
                node = node.right
        return upper

    # ...
    def get_predecessor(self, root, p):
        node, lower = root, None
        while node:
            if node.val < p.val:
                lower = node
                node = node.right
            else:
                node = node.left
        return lower
