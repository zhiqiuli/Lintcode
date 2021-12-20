"""
Definition of ListNode
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
    def mergeTwoLists(self, l1, l2):
        dummy      = ListNode(0)
        cur_node   = dummy

        while l1 and l2:
            if l1.val > l2.val:
                new_node = ListNode(l2.val)
                l2       = l2.next
            else:
                new_node = ListNode(l1.val)
                l1       = l1.next
            cur_node.next = new_node
            cur_node      = new_node

        while l1:
            new_node      = ListNode(l1.val)
            l1            = l1.next
            cur_node.next = new_node
            cur_node      = new_node

        while l2:
            new_node      = ListNode(l2.val)
            l2            = l2.next
            cur_node.next = new_node
            cur_node      = new_node

        return dummy.next
