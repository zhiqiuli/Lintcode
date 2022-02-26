'''
       1
     /   \
    3     2
   / \     \  
  5   3     9 


       0
     /   \
    0     1
   / \   / \  
  0   1 2   3 
'''

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
    @param root: the root
    @return: the maximum width of the given tree
    """
    def width_of_binary_tree(self, root: TreeNode) -> int:
        queue = collections.deque([(root, 0)]) # queue里面保存root和相应的位置，并且queue中都是有效的nodes
        max_width = 0
        while queue:
            n = len(queue)
            left = queue[0][1] # 此时不需要pop
            right = left
            for _ in range(n):
                node, right = queue.popleft()
                if node.left:
                    queue.append((node.left , right * 2    )) # 位置都是基于right的
                if node.right:
                    queue.append((node.right, right * 2 + 1))
                max_width = max(max_width, right - left + 1)
        return max_width
