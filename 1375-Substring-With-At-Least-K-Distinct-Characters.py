class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        total = 0
        for i in range(len(s)):
            res = {}
            for j in range(i, len(s)):
                if s[j] not in res:
                    res[s[j]]  = 1
                else:
                    res[s[j]] += 1
                if len(res) >= k:
                    total += (len(s) - j) # 这一步是关键
                    break
        return total
 
class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        ret = 0
        for i in range(len(s)):
            d = set()
            for j in range(i, len(s)):
                d.add(s[j]) # 使用set来存结果
                if len(d) >=k:
                    ret+=len(s)-j # 这一步是关键
                    break
        return ret
