class Solution:
    """
    @param n: an integer, denote the number of courses
    @param p: a list of prerequisite pairs
    @return: return an integer,denote the number of topologicalsort
    """
    def topologicalSortNumber(self, n, p):
        graph, indegree = self.buildGraph(n, p)
        visited = [0 for i in range(n)]
        memo = {}
        return self.dfs(n, graph, indegree, 0, visited, memo)

    def buildGraph(self, n, p):
        graph = {i:set() for i in range(n)}
        indegree = {i:0 for i in range(n)}
        for end, start in p:
            if end not in graph[start]:
                graph[start].add(end)
                indegree[end] += 1
        return graph, indegree
        
    def dfs(self, n, graph, indegree, count, visited, memo):
        if tuple(visited) in memo:
            return memo[tuple(visited)]
        
        if count == n:
            return 1

        num = 0
        for i in range(n):
            if visited[i] == 0 and indegree[i] == 0:
                visited[i] = 1
                for nb in graph[i]:
                    indegree[nb] -= 1
                num += self.dfs(n, graph, indegree, count + 1, visited, memo)
                for nb in graph[i]:
                    indegree[nb] += 1
                visited[i] = 0

        memo[tuple(visited)] = num
        
        return num
