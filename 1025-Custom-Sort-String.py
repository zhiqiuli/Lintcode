class Solution:
    """
    @param s: The given string S
    @param t: The given string T
    @return: any permutation of T (as a string) that satisfies this property
    """
    def custom_sort_string(self, S: str, T: str) -> str:
        dict_T, res = collections.Counter(T), ''
        for char in S:
            if char in dict_T:
                res += char * dict_T.pop(char) # char有类似list的assign方式 'a' * 5 = 'aaaaa'
        for char in sorted(dict_T):
            res += char * dict_T[char]
        return res
