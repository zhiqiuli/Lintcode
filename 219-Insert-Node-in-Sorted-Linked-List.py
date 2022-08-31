from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insert_node(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        dummy = ListNode(None, head)

        prev = dummy
        p    = head

        while p and p.val <= val:
            p    = p.next
            prev = prev.next

        new_node = ListNode(val)
        prev.next = new_node
        new_node.next = p

        return dummy.next
