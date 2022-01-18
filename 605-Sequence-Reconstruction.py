# https://www.lintcode.com/problem/605/?_from=collection&fromId=161

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.build_graph(seqs)
        return self.top_sort(graph) == org
    
    # 也可以直接写在主函数里，区别不大
    def top_sort(self, graph):
        indegree = self.get_indegree(graph)
        queue = collections.deque([x for x in indegree if indegree[x] == 0])
        top_order = []

        while queue:
            # 此时一定存在多种排序的可能性 直接返回None
            if len(queue) > 1:
                return None
            q = queue.popleft()
            top_order.append(q)
            for neighbor in graph[q]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # top_order长度和graph长度一样可以返回
        if len(top_order) == len(graph):
            return top_order
        # 这个函数return None
        return None

    # [1,2], [1,3] -> 1: (2, 3)
    # [1,4], [2,3] -> 1: (4) & 2: (3)
    # [5,2,6,3] -> 5:2, 2:6, 6:3, 3:()
    def build_graph(self, seqs):
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set() # set和list都可以，set应该更快一些

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i]) # 建立graph时依据的是前一个节点->下一个节点，[5,2,6,3] -> 5:2, 2:6, 6:3, 3:()
        
        return graph

    # 标准indegree模版
    def get_indegree(self, graph):
        indegree = {node : 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        
        return indegree
