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
    @param head: A ListNode.
    @return: A boolean.
    """
    def is_palindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        '''
        1->2->1    => mid=2
        1->2->3->1 => mid=3
        '''
        mid = self.find_mid(head)
        '''
        1->2    None<-2<-1 => mid=2
        1->2->3 None<-3<-1 => mid=3 所以不需要判断整个linked list的奇偶
        '''
        reversed_list = self.reverse(mid)
        while head and reversed_list:
            if head.val != reversed_list.val:
                return False
            head = head.next
            reversed_list = reversed_list.next
        return True

    # 直接背下来
    def reverse(self, head):
        prev = None
        while head:
            temp      = head.next
            head.next = prev
            prev      = head
            head      = temp
        return prev

    def find_mid(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow