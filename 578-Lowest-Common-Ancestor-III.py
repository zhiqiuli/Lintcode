关键点：
    1. dfs函数需要返回三个值，A是否在left，B是否在left，left的LCA（可以为None如果left没有LCA）

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        _, _, res = self.dfs(root, A, B)
        return res

    def dfs(self, root, A, B):
        if not root:
            return False, False, None
        
        # *****   Divide   *****
        left_a,  left_b,  left_node  = self.dfs(root.left , A, B)
        right_a, right_b, right_node = self.dfs(root.right, A, B)
        # (Boolean) left_a, left_b, whether A or B exist in the left subtree
        # (Boolean) right_a, right_b, whether A or B exist in the right subtree
        # left_node, right_node,  LCA of A and B in the left and right subtree

        # *****   Conquer   *****
        a = left_a or right_a or root == A
        b = left_b or right_b or root == B 

        # 根据 a和b 是否同时存在为初级判断条件
        # 然后再在第二层分类讨论，可能会比九章给出的参考答案更加思路清晰一些？ （仅供参考，欢迎提出批评指正）
        if a and b:
            #if left_node and right_node:
            #    # 因为左右子树都有存在的LCA，因此公共的LCA就是root本身
            #    return a, b, root
            if left_node: # 如果左子树存在LCA 返回左子树
                return a, b, left_node
            elif right_node: # 如果右子树存在LCA 返回右子树
                return a, b, right_node
            else:
                # 如果左右子树的LCA都不存在，那就只能是root这种情况了
                return a, b, root
        else:
            # 如果a 或 b 中有一个为False，就说明没有LCA，返回None
            return a, b, None
