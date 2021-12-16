import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.dict = dict()

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag = val not in self.dict
        self.data.append(val)
        idx = len(self.data) - 1
        if flag:
            self.dict[val] = set()

        self.dict[val].add(idx)
        return flag

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False

        last = self.data[-1]
        last_idx = len(self.data) - 1
        idx = self.dict[val].pop()

        if last_idx != idx: # index相同时则不需要
            self.dict[last].remove(last_idx)
        self.dict[last].add(idx)

        self.data[idx] = last
        self.data.pop()

        if not self.dict[val]:
            del self.dict[val]

        return True


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        idx = random.randint(0, len(self.data) - 1)
        return self.data[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
