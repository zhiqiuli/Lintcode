 # 与lintcode 7完全一样的

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
    @param data: a string after a tree serializing
    @return: the tree after a string deserialization
    """
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        
        TreeNodesBFS = [TreeNode(int(t)) if t != '#' else None for t in data.split(',')]
        root = TreeNodesBFS[0]

        # 此处也可以使用collections.deque([root])来实现 然后就不需要slow_index了
        nodes = [root]
        slow_index, fast_index = 0, 1

        # while fast_index < len(TreeNodesBFS):
        while slow_index < len(nodes):

            node = nodes[slow_index]
            slow_index += 1

            node.left  = TreeNodesBFS[fast_index]
            node.right = TreeNodesBFS[fast_index + 1]
            fast_index += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root

    """
    @param treeNode: A tree that needs to be serialized
    @return: the string after a tree serializing
    """
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ''
        
        queue = collections.deque([root])
        res = []

        while queue:
            node = queue.popleft()
            res.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)

        return ','.join(res)
