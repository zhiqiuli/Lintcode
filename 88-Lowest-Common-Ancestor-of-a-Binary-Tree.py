# https://www.lintcode.com/problem/88/?_from=collection&fromId=161

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        return self.helper(root, A, B)
    
    def helper(self, root, A, B):
        if root is None:
            return None

        # 如何遇到A，那LCA肯定是A，同理B
        if root is A or root is B:
            return root

        left  = self.helper(root.left , A, B)
        right = self.helper(root.right, A, B)

        # 结果在左边和右边 即返回root
        if left is not None and right is not None:
            return root
        # 结果在左边
        if left is not None:
            return left
        # 结果在右边
        if right is not None:
            return right
        return None
