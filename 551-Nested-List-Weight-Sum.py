"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object):
    def __init__(self):
        self.res = 0

    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        self.helper(nestedList, 1)
        return self.res
    
    def helper(self, nestedList, level):
        if type(nestedList) is list:
            for n_ in nestedList:
                self.helper(n_, level)
            return

        if nestedList.isInteger():
            self.res += (nestedList.getInteger() * level)
            return

        self.helper(nestedList.getList(), level + 1)
        return

    
    
class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        if not len(nestedList): return 0
        stack = []
        res = 0
        for n in nestedList:
            stack.append((n, 1))
        while stack:
            n, level = stack.pop()
            if n.isInteger():
                res += (n.getInteger() * level)
            else:
                for i in n.getList():
                    stack.append((i, level+1))
        return res
