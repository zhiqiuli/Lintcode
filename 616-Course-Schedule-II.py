# https://www.lintcode.com/problem/616/description?_from=collection&fromId=161

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        edges   = {i: [] for i in range(numCourses)}
        degrees = {i:  0 for i in range(numCourses)}

        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        
        queue = collections.deque([x for x in degrees if degrees[x] == 0])
        order = []

        while queue:
            q = queue.popleft()
            order.append(q)
            for n in edges[q]:
                degrees[n] -= 1
                if degrees[n] == 0:
                    queue.append(n)
        
        if len(order) == numCourses:
            return order
        else:
            return []
