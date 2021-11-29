# https://www.lintcode.com/problem/607/description?_from=collection&fromId=161

class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.count = {}
        
    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        for num in self.count:
            # make sure it won't count itself num
            if (value - num in self.count) and value - num != num:
                return True
            # duplicated elements and count > 1 say ..., 4, 4, ... target = 8
            if (value - num in self.count) and self.count[num] > 1:
                return True
        return False
