"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if not root:
            return []
        queue = collections.deque([root])
        res_all = []
        while queue: # 分层BFS
            res = []
            for _ in range(len(queue)):
                q = queue.popleft()
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
                res.append(q.val)
            res_all.append(res[:])
        
        res_ll = []
        for res in res_all:
            node = self.list2linkedlist(res)
            res_ll.append(node)
        
        return res_ll
        
    def list2linkedlist(self, res):
        dummy      = ListNode(0)
        p          = ListNode(res[0])
        dummy.next = p
        for val in res[1:]:
            p.next = ListNode(val)
            p      = p.next
        return dummy.next
