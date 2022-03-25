class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        min_len = min(len(s), len(t))
        for i in range(min_len):
            if s[i] != t[i]:
                # replace the different elements [...bDE, ..aDE] => [DE, DE]
                if len(s[i+1:]) == len(t[i+1:]):
                    return s[i+1:] == t[i+1:]
                # add or delete element in s
                return s[i+1:] == t[i:] or s[i:] == t[i+1:]
        # t maybe a substring of s, so make sure the diff is 1
        diff = abs(len(s) - len(t))
        return diff == 1
