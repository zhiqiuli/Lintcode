"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        # 双指针，一快&一慢
        q1, q2 = head, head.next
        while q2.next and q2.next.next:
            if q1 is q2:
                return True
            q1 = q1.next
            q2 = q2.next.next
        return False
