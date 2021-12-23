class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        n       = len(M)
        visited = [False] * n
        res     = 0
        for i in range(n):
            if not visited[i]:
                #print(i)
                visited[i] = True
                self.bfs(M, i, visited)
                res += 1
        return res
    
    def bfs(self, M, x, visited):
        deque = collections.deque([x])
        while deque:
            #print(deque)
            nowx = deque.popleft()
            for y in range(len(M)):
                #print(x, y, M[nowx][y])
                if not visited[y] and M[nowx][y]:
                    deque.append(y)
                    visited[y] = True
        return
