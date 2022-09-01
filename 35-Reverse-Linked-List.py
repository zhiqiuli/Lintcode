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
        '''
        prev  curr
        null  1   -> 2 -> 3 -> null
        
              prev   curr
        null<-1      2 -> 3 -> null

        reverse之后最后一个元素应该是None 所以prev从None开始
        '''
        prev, point = None, head # 
        while point:
            temp       = point.next # 注意！下一行的左边等于这一行的右边
            point.next = prev
            prev       = point
            point      = temp
        return prev
