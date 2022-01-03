"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            cur_res = []
            for _ in range(len(queue)):
                q = queue.popleft()
                cur_res.append(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            res.append(cur_res[:])
        return res[::-1]
