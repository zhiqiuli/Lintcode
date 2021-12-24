https://www.lintcode.com/problem/69/?_from=collection&fromId=161
层级遍历 - bfs
  
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            res0 = []
            for _ in range(len(queue)):
                node = queue.popleft()
                res0.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(res0[:])
        return res
