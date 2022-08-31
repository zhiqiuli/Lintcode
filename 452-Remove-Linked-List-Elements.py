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
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        dummy = ListNode(None, head)
        prev = dummy
        cur  = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur       = cur.next
            else:
                prev      = prev.next
                cur       = cur.next
        return dummy.next