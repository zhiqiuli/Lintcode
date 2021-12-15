https://www.lintcode.com/problem/105/description?_from=collection&fromId=161
'''
使用類似problem 137的方法，利用hash map 來建立映射關係，（node -> new node)
然後，再copy所有node的next以及random指針
'''
"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):

        if not head:
            return head
        
        mapping = {}
        curr = head
        while curr:
            mapping[curr] = RandomListNode(curr.label)
            curr = curr.next
        
        for node in mapping:
            if node.next:
                mapping[node].next = mapping[node.next]
            if node.random:
                mapping[node].random = mapping[node.random]
        
        return mapping[head]
