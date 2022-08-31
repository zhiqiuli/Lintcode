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
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swap_nodes(self, head: ListNode, v1: int, v2: int) -> ListNode:
        dummy = ListNode(None, head)
        prev = dummy
        curr = head
        node_list = []
        while head:
            if head.val == v1 or head.val == v2:
                node_list.append((prev, head))
            head = head.next
            prev = prev.next

        # not found values
        if len(node_list) < 2:
            return dummy.next

        prev_1, curr_1 = node_list[0][0], node_list[0][1]
        prev_2, curr_2 = node_list[1][0], node_list[1][1]

        prev_1.next, prev_2.next = prev_2.next, prev_1.next
        prev_1.next.next, prev_2.next.next = prev_2.next.next, prev_1.next.next
        return dummy.next

        if curr_1 != prev_2:
            end_node    = curr_2.next
            prev_1.next = curr_2
            curr_2.next = curr_1.next
            prev_2.next = curr_1
            curr_1.next = end_node
        else:
            end_node    = curr_2.next
            prev_1.next = curr_2
            curr_2.next = curr_1
            curr_1.next = end_node
        return dummy.next
