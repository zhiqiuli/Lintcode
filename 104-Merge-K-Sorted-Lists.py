方法1
使用counter可以避免重复当val相同时无法比较报错

import heapq
import itertools

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):

        if not lists:
            return None
        
        dummy = ListNode(0)
        tail = dummy
        heap = []
        counter = itertools.count()
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, next(counter), head))
        
        while heap:
            _, _, head = heapq.heappop(heap)
            tail.next = head
            tail = head
            if head.next:
                heapq.heappush(heap, (head.next.val, next(counter), head.next))
        
        return dummy.next
 
方法2

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return []
        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid   = (start + end) // 2
        left  = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.merge2Lists(left, right)

    def merge2Lists(self, a, b):
        dummy = ListNode(0)
        p_ = dummy

        while a and b:
            if a.val > b.val:
                p_.next = b
                b  = b.next
            else:
                p_.next = a
                a       = a.next
            p_ = p_.next
        
        if a: p_.next = a
        if b: p_.next = b

        return dummy.next
