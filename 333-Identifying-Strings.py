'''
Python, using a Trie. 我的思路是，看這個TrieNode在insert的階段時被走過幾次。後面找答案時，如果遇到的TrieNode只被走過一次，那走到該點的prefix就是能識別此string的shortest prefix。
'''
class TrieNode:
    def __init__(self):
        self.p = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
   
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.p:
                node.p[c] = TrieNode()
            node.count += 1
            node = node.p[c]
        node.count += 1
    
    def findShortestPrefix(self, word):
        node = self.root
        path = []
        for c in word:
            if c not in node.p:
                return ''

            node = node.p[c]
            path.append(c)
            if node.count == 1:
                return ''.join(path)

        return ''.join(path)

class Solution:
    """
    @param stringArray: a string array
    @return: return every strings'short peifix
    """
    def ShortPerfix(self, stringArray):
        trie = Trie()
        for word in stringArray:
            trie.insert(word)
        res = []
        for word in stringArray:
            res.append(trie.findShortestPrefix(word))
        return res
