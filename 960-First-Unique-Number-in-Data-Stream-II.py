https://www.lintcode.com/problem/960/description

class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.dummy       = ListNode(0)
        self.tail        = self.dummy
        self.num_to_prev = {}
        self.duplicates  = set()
    
    def add(self, num):
        # write your code here
        if num in self.duplicates:
            return
        
        if num not in self.num_to_prev:
            self.push_back(num)
            return
        
        # find duplicate, remove it from hash & linked list
        self.duplicates.add(num)
        self.remove(num)

    def remove(self, num):
        prev = self.num_to_prev[num]
        del self.num_to_prev[num]
        prev.next = prev.next.next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            # if we removed the tail node, prev will be the new tail
            self.tail = prev

    def firstUnique(self):
        if not self.dummy.next:
            return None
        return self.dummy.next.val
    
    # push a num to the tail
    def push_back(self, num):
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next
    

