class Solution:
    """
    @param word: a string
    @return: return a boolean
    """
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower():
            return True
        if len(word) > 1:
            if word[0].isupper() and word[1:].islower():
                return True
        return False
