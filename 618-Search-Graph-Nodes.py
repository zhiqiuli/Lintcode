# https://www.lintcode.com/problem/618/?_from=collection&fromId=161

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        queue = collections.deque([node])
        visited = set([node.label])
        while queue:
            for _ in range(len(queue)): # 最短路径！
                q = queue.popleft()
                if values[q] == target: # 放在这里是因为有可能起点即是终点 并且起点没有邻居点
                    return q
                for q_next in q.neighbors:
                    if q_next.label in visited:
                        continue
                    queue.append(q_next)
                    visited.add(q_next.label)
        return None
