from typing import (
    List,
)

class Solution:
    """
    @param rating: the rating of the movies
    @param g: the realtionship of movies
    @param s: the begin movie
    @param k: top K rating 
    @return: the top k largest rating moive which contact with S
    """
    def top_k_movie(self, rating: List[int], g: List[List[int]], s: int, k: int) -> List[int]:
        
        visited = set([s])
        queue = collections.deque([s])
        
        # min heap可以保存最大的前k项
        import heapq
        h = []

        while queue:
            n = queue.popleft()
            for i in g[n]:
                if i in visited:
                    continue

                visited.add(i)
                queue.append(i)
                
                heapq.heappush(h, [rating[i], i])

                if len(h) > k:
                    heapq.heappop(h)

        print(h)
        return [x[1] for x in h]
