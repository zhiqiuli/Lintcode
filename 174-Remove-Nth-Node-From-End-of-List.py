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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        dummy = ListNode(None, head)

        # fast moves n steps first
        fast = head
        for _ in range(n):
            fast = fast.next

        # fast moves to the end
        prev = dummy
        curr = head
        while fast:
            fast = fast.next
            curr = curr.next
            prev = prev.next

        # skip the curr
        prev.next = curr.next

        return dummy.next
