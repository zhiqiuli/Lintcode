class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        if not s:
            return 0
        counter = {}
        left    = 0
        result  = 0
        maxlen  = 0
        for right in range(len(s)):
            if s[right] not in counter:
                counter[s[right]]  = 1
            else:
                counter[s[right]] += 1
            maxlen = max(maxlen, counter[s[right]])
            if right - left + 1 - maxlen > k: # 已经不能再进行替换操作了 移动窗口左边
                counter[s[left]] -= 1
                left += 1
            else:
                result = max(result, right - left + 1)
        return result
