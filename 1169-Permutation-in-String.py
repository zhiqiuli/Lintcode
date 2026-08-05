from collections import Counter, defaultdict
class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def check_inclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        if count1 == count2:
            return True
        for i in range(n1, n2):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - n1]) - ord('a')] -= 1
            if count1 == count2:
                return True
        return False