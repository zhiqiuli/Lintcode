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
    @param root: the root
    @return: all the values with the highest frequency in any order
    """
    def find_frequent_tree_sum(self, root: TreeNode) -> List[int]:
        res = {}
        self.dfs(root, res)
        most_freq = -sys.maxsize
        for key in res:
            most_freq = max(most_freq, res[key])
        final_res = []
        for key in res:
            if res[key] == most_freq:
                final_res.append(key)
        return final_res
    
    def dfs_sum(self, node):
        if node is None:
            return 0
        cur_sum = node.val + self.dfs_sum(node.left) + self.dfs_sum(node.right)
        return cur_sum
    
    def dfs(self, node, res):
        if node is None:
            return
        cur_res = self.dfs_sum(node)
        res[cur_res] = res.get(cur_res, 0) + 1
        self.dfs(node.left , res)
        self.dfs(node.right, res)
