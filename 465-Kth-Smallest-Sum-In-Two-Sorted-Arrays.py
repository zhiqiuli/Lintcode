import heapq
class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        n, m = len(A), len(B)
        visited = set([0])
        h = []
        heapq.heappush(h, (A[0] + B[0], 0, 0))
        for _ in range(k):
            num, x, y = heapq.heappop(h) # 每次添加(x+1, y)和(x, y+1)
            if x + 1 < n and (x + 1) * m + y not in visited: # visit也可以存坐标 这种写法其实和坐标也有1-1对应
                heapq.heappush(h, (A[x + 1] + B[y], x + 1, y))
                visited.add((x + 1) * m + y)
            if y + 1 < m and x * m + y + 1 not in visited:
                heapq.heappush(h, (A[x] + B[y + 1], x, y+1))
                visited.add(x * m + y + 1)
        return num
