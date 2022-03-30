* Price
* Tree Traversal

Version 1

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root):
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

Version 2

cindychen0204 Publish at 2021-02-27

仔细想一下，只有第一种方法改过来时最方便的。
需要的改动仅仅调换一下节点访问的次序，先序是先访问，再入栈；
而中序则是先入栈，弹栈后再访问

但是感覺有走過同樣一條路

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        result = []
        stack = []
        
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            curNode = stack.pop()
            result.append(curNode.val)
            
            if curNode.right:
                curNode = curNode.right
                while curNode:
                    stack.append(curNode)
                    curNode = curNode.left
        
        return result
