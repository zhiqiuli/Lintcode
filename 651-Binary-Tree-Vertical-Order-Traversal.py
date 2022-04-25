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
        queue = collections.deque()
        results = collections.defaultdict(list) # 使用defaultdict，默认的类别是list
        queue.append((0, root))
        while queue:
            pos, node = queue.popleft()
            if node:
                results[pos].append(node.val)
                queue.append((pos - 1, node.left))
                queue.append((pos + 1, node.right))
        return [results[i] for i in sorted(results)] # O(Nlog(N))
