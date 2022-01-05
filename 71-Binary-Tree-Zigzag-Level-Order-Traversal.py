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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            path = []
            for _ in range(len(queue)):
                q = queue.popleft()
                path.append(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            res.append(path[:])

        # reverse even numbers
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        
        return res
