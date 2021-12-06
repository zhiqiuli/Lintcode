# https://www.lintcode.com/problem/1790/?_from=collection&fromId=161
class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        if left > right:
            offset = (left - right) % len(str)
            return str[ offset:] + str[: offset]
        elif right > left:
            offset = (right - left) % len(str)
            return str[-offset:] + str[:-offset]
        else:
            return str
