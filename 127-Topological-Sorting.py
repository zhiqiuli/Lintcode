# https://www.lintcode.com/problem/127/?_from=collection&fromId=161

"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        order = []
        node_to_indegree = self.get_indegree(graph)
        queue = collections.deque([x for x in node_to_indegree if node_to_indegree[x] == 0])
        # level = 0 (*)
        while queue:
            # for _ in range(len(queue) (*)
            q = queue.popleft()
            order.append(q)
            for n in q.neighbors:
                node_to_indegree[n] -= 1 # order.append()以后就需要indegree-1
                if node_to_indegree[n] == 0: # 如何indgegree成为0，自然放进queue当中
                    queue.append(n)
            # level += 1 (*)
        
        return order
    # (*) means if we want to make sure that ***how many levels we need in order to cover all the nodes***.
    
    # find nodes with indegree == 0
    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}
        for node in graph:
            for n in node.neighbors:
                node_to_indegree[n] += 1
        return node_to_indegree
