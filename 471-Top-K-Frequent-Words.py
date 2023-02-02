from typing import (
    List,
)

import heapq

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def top_k_frequent_words(self, words: List[str], k: int) -> List[str]:

        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1

        # 比较简单的做法就是先把所有元素存下来，然后再pop前k个元素
        h = []
        heapq.heapify(h)
        for key, val in dic.items():
            heapq.heappush(h, (-val, key))

        res = []
        for _ in range(k):
            val, key = heapq.heappop(h)
            res.append(key)
        
        return res
