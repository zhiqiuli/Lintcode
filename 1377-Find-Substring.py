class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """
    def find_substring(self, str: str, k: int) -> int:
        res = set()
        cur = []
        left, right = 0, 0

        # while好处在于每次移动either left或者right；
        # 假设使用for loop，那么right每次都会移动。
        # 考虑这种情况：假设到了下一位出现重复的话，只需要移动left
        while right < len(str):

            if str[right] not in cur:
                cur.append(str[right])
                right += 1
                
                if len(cur) == k:
                    cur_str = ''.join(cur)
                    if cur_str not in res:
                        res.add(cur_str)
                    left += 1
                    del cur[0]            
            else:
                left += 1
                del cur[0]
                continue

        return len(res)
