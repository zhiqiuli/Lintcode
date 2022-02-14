"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if not head or not head.next: return head
        prev, point = None, head # reverse之后最后一个元素应该是None 所以prev从None开始
        while point:
            temp = point.next
            point.next = prev
            prev = point
            point = temp
        return prev
