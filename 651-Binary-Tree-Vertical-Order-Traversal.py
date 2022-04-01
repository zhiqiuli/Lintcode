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
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        pos   = 0
        ###
        ### BFS用queue
        ###
        queue = collections.deque([(pos, root)])
        node_per_level = {}
        while queue:
            pos_, node = queue.popleft()
            if node:
                if pos_ in node_per_level:
                    node_per_level[pos_].append(node.val)
                else:
                    node_per_level[pos_] = [node.val]
                queue.append((pos_ - 1, node.left ))
                queue.append((pos_ + 1, node.right))
        res = []
        for key in sorted(node_per_level.keys()):
            res.append(node_per_level[key][:])
        return res
