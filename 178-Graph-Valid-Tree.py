# https://www.lintcode.com/problem/178/description?_from=collection&fromId=161

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # 是树的条件1 保证不存在有环 边数 == 节点数 - 1
        if len(edges) != n - 1:
            return False

        graph = {i:[] for i in range(n)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        # 是树的话 从0节点开始游览
        queue = collections.deque([0])
        visit = set([0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)

        return len(visit) == n
