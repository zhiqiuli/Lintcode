# https://www.lintcode.com/problem/120/description?_from=collection&fromId=161

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end) # make sure the last element is saved in the result dict
        queue = collections.deque([start])
        visited = set([start])
        distance = 0

        while queue:
            distance += 1            
            for _ in range(len(queue)): # 简单图最短路径，分层bfs，需要range(len(queue))
                word = queue.popleft()
                if word == end:
                    return distance
                
                # total is O(26*L^2)
                for next_word in self.find_next_words(word, dict):
                    if next_word not in dict or next_word in visited: # O(L)
                        continue
                    queue.append(next_word)
                    visited.add(next_word)

        return 0
    
    def find_next_words(self, word, dictionary):
        words = []
        for i in range(len(word)): # O(L)
            left, right = word[:i], word[i+1:]
            for k in 'qwertyuiopasdfghjklzxcvbnm': # O(26)
                if word[i] == k: # make sure the same one is not included
                    continue
                words.append(left + k + right)
        return words
