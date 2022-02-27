from typing import (
    List,
)

class Solution:
    """
    @param s: a string
    @return: a list of integers representing the size of these parts
    """
    def partition_labels(self, s: str) -> List[int]:
        char_to_last_occurs = {}
        for i in range(len(s) - 1, -1, -1):
            char_to_last_occurs[s[i]] = char_to_last_occurs.get(s[i], i)
        res = []
        left, right = 0, 0
        while right < len(s):
            char = s[right]
            right = char_to_last_occurs[char]
            i = left
            while i < right:
                right = max(right, char_to_last_occurs[s[i]])
                i += 1
            # 保存结果
            res.append(right - left + 1)
            # 同时move left和right
            right += 1
            left = right
        return res
