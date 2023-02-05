from collections import Counter
import heapq
class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reorganize_string(self, s: str) -> str:
        counter = Counter(s)
        maxCount = max([item[1] for item in counter.items()])
        # 最大长度 (4+1)//2=2 & (3+1)//2=2
        # 4 - aabb (max=2 good)
        #     aaab (max=3 not good)
        if maxCount > (len(s) + 1) // 2:
            return ''
        queue = [(-val[1], val[0]) for val in counter.items()]
        heapq.heapify(queue)
        ans = []
        while len(queue) > 1:
            # 每次pop两个，确保两个不相同
            _, char1 = heapq.heappop(queue)
            _, char2 = heapq.heappop(queue)
            ans.append(char1)
            ans.append(char2)
            counter[char1] -= 1
            counter[char2] -= 1
            if counter[char1] > 0:
                heapq.heappush(queue, (-counter[char1], char1))
            if counter[char2] > 0:
                heapq.heappush(queue, (-counter[char2], char2))
        # 开始的maxCount条件保证了最后queue的长度只能为1
        if queue:
            ans.append(queue[0][1])
        
        return ''.join(ans)