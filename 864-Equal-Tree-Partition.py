"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def checkEqualTree(self, root):
        return self.dfs(root)
    
    def dfs(self, root):
        if root is None:
            return False

        left_sum  = self.pathSum(root.left)
        right_sum = self.pathSum(root.right)

        if left_sum + root.val == right_sum or left_sum == right_sum + root.val:
            return True
        
        self.dfs(root.left)
        self.dfs(root.right)

        return False

    def pathSum(self, root):
        if root is None:
            return 0
        return root.val + self.pathSum(root.left) + self.pathSum(root.right)

    
    
    
    
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def checkEqualTree(self, root):
        self.memo = {}
        total_sum = self.traverse(root)
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            curr_sum = self.traverse(node)
            if node != root and total_sum - curr_sum == curr_sum:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def traverse(self, root):
        if root is None:
            return 0

        if root in self.memo:
            return self.memo[root]

        self.memo[root] = root.val
        self.memo[root] += self.traverse(root.left)
        self.memo[root] += self.traverse(root.right)
        
        return self.memo[root]
