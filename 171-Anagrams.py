class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        hash_table = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in hash_table:
                hash_table[sorted_str] =  1
            else:
                hash_table[sorted_str] += 1
        
        res = []
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if hash_table[sorted_str] > 1:
                res.append(str)

        return res
