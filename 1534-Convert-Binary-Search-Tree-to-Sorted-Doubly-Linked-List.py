"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        if root is None:
            return None, None
            
        head, tail = self.dfs(root)
        
        # 因为题目要求是环，所以还要首尾相连
        tail.right = head
        head.left  = tail

        return head
    
    def dfs(self, root):
        if root is None:
            return None, None
            
        left_head , left_tail  = self.dfs(root.left )
        right_head, right_tail = self.dfs(root.right)

        # left tail <-> root
        if left_tail:
            left_tail.right = root
            root.left = left_tail
        
        # root <-> right_head
        if right_head:
            right_head.left = root
            root.right = right_head
        
        # 此处or前后elements的顺序很重要
        tail = right_tail or root # or left_tail
        head = left_head or root # or right_head

        return head, tail
