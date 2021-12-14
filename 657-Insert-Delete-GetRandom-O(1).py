'''
使用数组来保存当前集合中的元素，同时用一个hashMap来保存数字与它在数组中下标的对应关系。

插入操作时：

若已存在此元素返回false
不存在时将新的元素插入数组最后一位，同时更新hashMap。
删除操作时：

若不存在此元素返回false
存在时先根据hashMap得到要删除数字的下标，再将数组的最后一个数放到需要删除的数的位置上，删除数组最后一位，同时更新hashMap。
获取随机数操作时：

根据数组的长度来获取一个随机的下标，再根据下标获取元素。
'''
import random

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.nums, self.val_to_key = [], {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.val_to_key:
            return False
        self.nums.append(val)
        self.val_to_key[val] = len(self.nums) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.val_to_key:
            return False
        
        index = self.val_to_key[val]
        last  = self.nums[-1]

        # move last one to index
        self.nums[index]      = last
        self.val_to_key[last] = index

        # pop and remove
        self.nums.pop()
        del self.val_to_key[val]

        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
