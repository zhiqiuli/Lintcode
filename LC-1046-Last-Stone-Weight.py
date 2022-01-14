class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        h = []
        for i in stones: heapq.heappush(h, -i)
        while h:
            print(h)
            if len(h) == 1:
                return -h[0]
            if len(h) == 2:
                s1, s2 = -h[0], -h[1]
                if s1 == s2:
                    return 0
                elif s1 > s2:
                    return s1 - s2
                else:
                    return s2 - s1
            
            s1 = -heapq.heappop(h)
            s2 = -heapq.heappop(h)
            if s1 == s2:
                continue
            elif s1 > s2:
                heapq.heappush(h, - s1 + s2)
            else:
                heapq.heappush(h, - s2 + s1)
        
        return 0
