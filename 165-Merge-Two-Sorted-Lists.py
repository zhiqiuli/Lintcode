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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        dummy = ListNode(0)
        curr  = dummy
        while l1 and l2:
            if l1.val >= l2.val:
                new_node = ListNode(l2.val)
                l2 = l2.next
                curr.next = new_node
                curr = curr.next
            else:
                new_node = ListNode(l1.val)
                l1 = l1.next
                curr.next = new_node
                curr = curr.next
        
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        
        return dummy.next