"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        queue = collections.deque([s])
        seen = set([s.label])
        dist = 0
        while queue:
            for _ in range(len(queue)):
                q = queue.popleft()
                if q.label == t.label:
                    return dist
                for nb in q.neighbors:
                    if nb.label not in seen:
                        queue.append(nb)
                        seen.add(nb.label)
            dist += 1
        return -1
