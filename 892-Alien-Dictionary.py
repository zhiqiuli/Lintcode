# https://www.lintcode.com/problem/892/description?_from=collection&fromId=161

from heapq import *
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Construct Graph
        # 使用双重list comprehensive 忽略掉重复的key
        in_degree = {ch: 0 for word in words for ch in word}
        neighbors = {ch: [] for word in words for ch in word}

        # from "wrt"and"wrf" ,we can get 't'<'f'
        # e.g. in_degree['t'] += 1
        #      neighbors['f'] = [t]
        for pos in range(len(words) - 1):
            for i in range(min(len(words[pos]), len(words[pos + 1]))):
                pre, next = words[pos][i], words[pos + 1][i]
                if pre != next:
                    in_degree[next] += 1
                    neighbors[pre].append(next)
                    break
            '''
            notice when check the last element, if ['abc', 'ab'], then there is no valid order for this case
            if ['abcd', 'abd'], this is apparenly valid case
            '''
            if pre == next and len(words[pos]) > len(words[pos + 1]):
                return ''

        # Topological Sort
        # 必须使用heap保证最小的lexicographical order
        heap = [ch for ch in in_degree if in_degree[ch] == 0]
        heapify(heap)
        order = []
        while heap:
            for _ in range(len(heap)):
                ch = heappop(heap)
                order.append(ch)
                for child in neighbors[ch]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        heappush(heap, child)
        
        # order is invalid
        if len(order) != len(in_degree):
            return ""
        return ''.join(order)
