import heapq

class TopK:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.word_to_count = {}
        self.cap = k
        # 用count做index, 记录每个count 下有啥词
        # 0 count 对应的hashset 一直为空  
        self.count_to_words = [set()]

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        prev_count = self.word_to_count.get(word, 0)
        self.word_to_count[word] = prev_count + 1

        # 如果word之前出现过，就先把它从旧的count里移除
        if prev_count != 0:
            self.count_to_words[prev_count].remove(word)
        
        # 找到对应的count把word加进去，可能要扩展count_to_words
        if prev_count + 1 < len(self.count_to_words):
            self.count_to_words[prev_count + 1].add(word)
        else:
            self.count_to_words.append(set([word]))

    """
    @return: the current top k frequent words.
    """
    def topk(self):
        # 从 count_to_words中倒着找全k个高频词
        k = self.cap
        res = []
        i = len(self.count_to_words) - 1
        while k and i > -1:
            words = sorted(self.count_to_words[i])
            for word in words:
                res.append(word)
                k -= 1
                if k == 0:
                    return res
            i -= 1
        return res
            
