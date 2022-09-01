方法1

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

        return self.mergeRangeLists(0, len(lists) - 1, lists)
    
    def mergeRangeLists(self, left, right, lists):
        
        if left == right:
            return lists[left]
        
        mid = (left + right) // 2
        
        l1 = self.mergeRangeLists(left   , mid  , lists)
        l2 = self.mergeRangeLists(mid + 1, right, lists)

        return self.merge2Lists(l1, l2)
    
    def merge2Lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        curr  = dummy
        while l1 and l2:
            if l1.val >= l2.val:
                new_node = ListNode(l2.val)
                l2 = l2.next
                curr.next = new_node
                curr      = curr.next
            else:
                new_node = ListNode(l1.val)
                l1 = l1.next
                curr.next = new_node
                curr      = curr.next

        if l1:
            curr.next = l1

        if l2:
            curr.next = l2

        return dummy.next
        


方法2
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