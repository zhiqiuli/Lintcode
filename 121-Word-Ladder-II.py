# https://www.lintcode.com/problem/121/description?_from=collection&fromId=161

'''
从 end 到 start 做一次 BFS，并且把距离 end 的距离都保存在 distance 中。
然后在从 start 到 end 做一次 DFS，每走一步必须确保离 end 的 distance 越来越近。

与另外一个代码中提前建立 index 不同，这里是在寻找下一个变换单词的时候，再去获得对应的单词列表。一个单词最多有 L 个字符，每个字符有 25 种不同的变化（26个字母除掉这个位置上的字母），然后 check 一下在不在 dict 里就知道是不是 next word 了。
'''

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        res = []
        dict.add(start)
        dict.add(end)
        distance = {}
        self.bfs(end, distance, dict)
        self.dfs(start, end, dict, start, [start], distance, res)
        return res

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = collections.deque([start])
        while queue:
            word = queue.popleft()
            words = self.get_next_words(word, dict)
            for next_word in words:
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def dfs(self, start, end, dict, word, chars, distance, res):
        if word == end:
            res.append(chars[:])
            return

        words = self.get_next_words(word, dict)
        for new_word in words:
            if distance[new_word] != distance[word] - 1:
                continue
            chars.append(new_word)
            self.dfs(start, end, dict, new_word, chars, distance, res)
            chars.pop()

    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for l in 'qwertyuiopasdfghjklzxcvbnm':
                if word[i] == l:
                    continue
                new_word = word[:i] + l + word[i+1:]
                if new_word in dict:
                    words.append(new_word)
        return words
