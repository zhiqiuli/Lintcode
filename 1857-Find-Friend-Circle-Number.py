from typing import (
    List,
)

class Solution:
    """
    @param m: a matrix of integer
    @return: return an Integer
    """
    def find_circle_num(self, circle: List[List[int]]) -> int:
        n = len(circle)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if circle[i][j] == 1:
                    uf.merge(i, j)
        print(uf.father)
        return uf.cnt

class UnionFind():
    def __init__(self, n):
        self.cnt    = n
        self.father = [i for i in range(n)]
        self.rank   = [0] * n
            
    def find(self, a):
        while self.father[a] != a:
            a = self.find(self.father[a])
        return self.father[a]

    def merge(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return
        if self.rank[root_a] > self.rank[root_b]:
            self.father[root_b] = root_a
        elif self.rank[root_a] < self.rank[root_b]:
            self.father[root_a] = root_b
        else:
            self.father[root_b] = root_a;
            self.rank[root_a] += 1
        self.cnt -= 1
