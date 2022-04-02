class Solution:

    def preorderTraversal(self, root):
        if root is None: return []

        stack = [root]
        preorder = []
        
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder



后续遍历是先左子树，再右子树再到父结点，倒过来看就是先父结点，再右子树再左子树。
是前序遍历改变左右子树访问顺序。
再将输出的结果倒序输出一遍就是后序遍历。

class Solution:

    def postorderTraversal(self, root):
        if root is None: return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]



class Solution:

    def inorderTraversal(self, root):
        if not root: return []
        
        result = []
        stack = []
        
        # 1.先走到最左下角
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            # 2.pop的时候把元素append到res
            curNode = stack.pop()
            result.append(curNode.val)
            
            # 3.当right存在时再走一步right
            if curNode.right:
                curNode = curNode.right
                # 4.和1.很相似
                while curNode:
                    stack.append(curNode)
                    curNode = curNode.left
        
        return result
