# https://www.lintcode.com/problem/431/description?_from=collection&fromId=161

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        visited = set()
        res = []

        for node in nodes: # 浏览每个节点 并不需要存贮边的信息
            if node.label in visited:
                continue

            queue = collections.deque([node])
            visited.add(node.label)
            order = [node.label] # 此节点的答案
            while queue:
                q = queue.popleft()
                for neighbor in q.neighbors:
                    if neighbor.label in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor.label)
                    order.append(neighbor.label)
            res.append(sorted(order)) # 结果要求进行排序

        return res
