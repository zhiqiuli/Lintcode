https://www.lintcode.com/problem/685/description?_from=collection&fromId=161
  
class Solution:

    def __init__(self):
        self.dummy       = ListNode(0)
        self.tail        = self.dummy
        self.num_to_prev = {}
        self.duplicates  = set()

    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        for num in nums:
            self.add(num)
            if num == number:
                return self.dummy.next.val
        return -1

    def add(self, num):
        if num in self.duplicates:
            return
        
        if num not in self.num_to_prev:
            self.push_back(num)
            return

        self.duplicates.add(num)
        self.remove(num)
    
    def remove(self, num):
        prev = self.num_to_prev[num]
        del self.num_to_prev[num]
        prev.next = prev.next.next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            # if the tail is removed
            self.tail = prev

    def push_back(self, num):
        # new num add to the tail
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next
