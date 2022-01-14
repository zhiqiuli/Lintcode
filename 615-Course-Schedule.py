# https://www.lintcode.com/problem/615/description?_from=collection&fromId=161

class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        edges  = {i: [] for i in range(numCourses)} 
        degree = {i: 0  for i in range(numCourses)} # 记录每个node的indegree是多少
        for i, j in prerequisites:
            edges[j].append(i)
            degree[i] += 1
        
        queue = collections.deque([x for x in degree if degree[x] == 0])
        level = 0
        while queue:
            level += 1
            q = queue.popleft()
            for n in edges[q]:
                degree[n] -= 1
                if degree[n] == 0: # queue中都是indegree为0的nodes
                    queue.append(n)
        return numCourses == level
