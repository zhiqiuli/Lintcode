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
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):

        inorder = self.get_inorder(root)
        left = self.find_lower_index(inorder, target)
        right = left + 1
        res = []
        for _ in range(k):
            if self.left_is_closer(inorder, target, left, right):
                res.append(inorder[left])
                left -= 1
            else:
                res.append(inorder[right])
                right += 1
        return res
    
    # obtain inorder traversal array
    def get_inorder(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        inorder = []
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)
        return inorder
    
    #
    def find_lower_index(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid
        
        if A[right] < target:
            return right
        if A[left] < target:
            return left
        
        return -1
    
    def left_is_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        if abs(A[left] - target) < abs(A[right] - target):
            return True
        return False
