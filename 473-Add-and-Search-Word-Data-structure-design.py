class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        return self.dfs(word, self.root, 0)
    
    def dfs(self, word, node, index):
        if len(word) == index:
            return node.is_word

        char = word[index]
        if char != '.':
            if char not in node.children:
                return False
            return self.dfs(word, node.children[char], index + 1)
        
        for child in node.children:
            if self.dfs(word, node.children[child], index + 1):
                return True
        
        return False
