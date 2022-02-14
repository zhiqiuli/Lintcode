"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        num1 = self.list2num(l1)
        num2 = self.list2num(l2)
        return self.num2list(str(num1 + num2))
    
    def num2list(self, num):
        head = ListNode(0)
        prev = head
        while len(num):
            curr = ListNode(num[-1])
            prev.next = curr
            prev = curr
            curr = curr.next
            num = num[:-1]
        return head.next
    
    def list2num(self, l):
        num = 0
        dec = 0
        p = l
        while p:
            num += p.val * (10 ** dec)
            dec += 1
            p = p.next
        return num
