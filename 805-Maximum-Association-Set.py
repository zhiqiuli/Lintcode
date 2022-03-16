from typing import (
    List,
)

class Solution:
    """
    @param list_a: The relation between ListB's books
    @param list_b: The relation between ListA's books
    @return: The answer
    """
    def maximum_association_set(self, list_a: List[str], list_b: List[str]) -> List[str]:
        uf = UnionFind()
        for i in range(len(list_a)):
            uf.add(list_a[i])
            uf.add(list_b[i])
            uf.merge(list_a[i], list_b[i])
            
            '''
            print(i, uf.father)
            
            ["a","b","d","e","f"]
            ["b","c","e","g","g"]

            0 {'a': 'b', 'b': ['b', 'a']}
            1 {'a': 'b', 'b': 'c', 'c': ['c', 'b', 'a']}
            2 {'a': 'b', 'b': 'c', 'c': ['c', 'b', 'a'], 'd': 'e', 'e': ['e', 'd']}
            3 {'a': 'b', 'b': 'c', 'c': ['c', 'b', 'a'], 'd': 'e', 'e': 'g', 'g': ['g', 'e', 'd']}
            4 {'a': 'b', 'b': 'c', 'c': ['c', 'b', 'a'], 'd': 'e', 'e': 'g', 'g': ['g', 'e', 'd', 'f'], 'f': 'g'}
            '''
            
        return uf.father[uf.max_root]

        

class UnionFind():
    def __init__(self):
        self.father = {}
        self.max_size = 0
        self.max_root = ""

    def add(self, a):
        if a not in self.father:
            self.father[a] = [a]

    def find(self, a):
        # 只保存了最长的father
        if isinstance(self.father[a], list):
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def merge(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        # father[root_a]或father[root_b]其中有一个可能是list
        # merge以后只保存一个list
        if root_a != root_b:
            self.father[root_b].extend(self.father[root_a])
            self.father[root_a] = root_b
            if len(self.father[root_b]) > self.max_size:
                self.max_root = root_b
                self.max_size = len(self.father[root_b])

