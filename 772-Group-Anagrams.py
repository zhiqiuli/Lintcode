class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        dic = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            dic[sorted_word] = dic.get(sorted_word, []) + [word]
        return dic.values()
