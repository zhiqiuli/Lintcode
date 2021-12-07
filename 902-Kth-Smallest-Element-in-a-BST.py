"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        ### 考察如何实现iteration bst
        ### inorder iteration tree 模版题
        ### 创建一个dummy node，右指针指向root
        ### 并放在stack里，此时stack的栈顶是dummy
        ### 是iterator的位置
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for _ in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if not stack:
                return None
                
        return stack[-1].val
